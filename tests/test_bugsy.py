import json

import pytest
import responses

from bugsy import Bugsy, Bug
from bugsy.errors import BugsyException, LoginException
from . import rest_url


def test_we_cant_post_without_a_username_or_password():
    bugzilla = Bugsy()
    with pytest.raises(BugsyException) as e:
        bugzilla.put("foo")
    assert (
        str(e.value)
        == "Message: Unfortunately you can't put bugs in Bugzilla without credentials Code: None"
    )


@responses.activate
def test_we_get_a_login_exception_when_details_are_wrong():
    responses.add(
        responses.GET,
        "https://bugzilla.mozilla.org/rest/login",
        body='{"message": "The username or password you entered is not valid."}',
        status=400,
        content_type="application/json",
    )
    with pytest.raises(LoginException) as e:
        Bugsy("foo", "bar")
    assert (
        str(e.value)
        == "Message: The username or password you entered is not valid. Code: None"
    )
    assert responses.calls[0].request.headers["X-Bugzilla-Login"] == "foo"
    assert responses.calls[0].request.headers["X-Bugzilla-Password"] == "bar"


@responses.activate
def test_bad_api_key():
    responses.add(
        responses.GET,
        "https://bugzilla.mozilla.org/rest/valid_login?login=foo",
        body='{"documentation":"http://www.bugzilla.org/docs/tip/en/html/api/","error":true,"code":306,"message":"The API key you specified is invalid. Please check that you typed it correctly."}',
        status=400,
        content_type="application/json",
    )
    with pytest.raises(LoginException) as e:
        Bugsy(username="foo", api_key="badkey")
    assert (
        str(e.value)
        == "Message: The API key you specified is invalid. Please check that you typed it correctly. Code: 306"
    )
    assert responses.calls[0].request.headers["X-Bugzilla-API-Key"] == "badkey"


@responses.activate
def test_validate_api_key():
    responses.add(
        responses.GET,
        "https://bugzilla.mozilla.org/rest/valid_login?login=foo",
        body="true",
        status=200,
        content_type="application/json",
    )
    Bugsy(username="foo", api_key="goodkey")
    assert responses.calls[0].request.headers["X-Bugzilla-API-Key"] == "goodkey"


@responses.activate
def test_we_cant_post_without_passing_a_bug_object():
    responses.add(
        responses.GET,
        "https://bugzilla.mozilla.org/rest/login",
        body='{"token": "foobar"}',
        status=200,
        content_type="application/json",
    )
    bugzilla = Bugsy("foo", "bar")
    with pytest.raises(BugsyException) as e:
        bugzilla.put("foo")
    assert (
        str(e.value)
        == "Message: Please pass in a Bug object when posting to Bugzilla Code: None"
    )


@responses.activate
def test_we_can_get_a_bug(bug_return):
    responses.add(
        responses.GET,
        rest_url("bug", 1017315),
        body=json.dumps(bug_return),
        status=200,
        content_type="application/json",
    )
    bugzilla = Bugsy()
    bug = bugzilla.get(1017315)
    assert bug.id == 1017315
    assert bug.status == "RESOLVED"
    assert bug.summary == "Schedule Mn tests on opt Linux builds on cedar"


@responses.activate
def test_we_can_get_a_bug_with_login_token(bug_return):
    responses.add(
        responses.GET,
        "https://bugzilla.mozilla.org/rest/login",
        body='{"token": "foobar"}',
        status=200,
        content_type="application/json",
    )
    responses.add(
        responses.GET,
        rest_url("bug", 1017315),
        body=json.dumps(bug_return),
        status=200,
        content_type="application/json",
    )
    bugzilla = Bugsy("foo", "bar")
    bug = bugzilla.get(1017315)
    assert bug.id == 1017315
    assert bug.status == "RESOLVED"
    assert bug.summary == "Schedule Mn tests on opt Linux builds on cedar"
    assert responses.calls[1].request.headers["X-Bugzilla-Token"] == "foobar"


@responses.activate
def test_we_can_get_username_with_userid_cookie():
    responses.add(
        responses.GET,
        "https://bugzilla.mozilla.org/rest/user/1234",
        body='{"users": [{"name": "user@example.com"}]}',
        status=200,
        content_type="application/json",
    )

    bugzilla = Bugsy(userid="1234", cookie="abcd")
    assert bugzilla.username == "user@example.com"
    assert responses.calls[0].request.headers["X-Bugzilla-Token"] == "1234-abcd"


@responses.activate
def test_we_can_create_a_new_remote_bug():
    bug = Bug()
    bug.summary = "I like foo"
    responses.add(
        responses.GET,
        "https://bugzilla.mozilla.org/rest/login",
        body='{"token": "foobar"}',
        status=200,
        content_type="application/json",
    )
    bug_dict = bug.to_dict().copy()
    bug_dict["id"] = 123123
    responses.add(
        responses.POST,
        "https://bugzilla.mozilla.org/rest/bug",
        body=json.dumps(bug_dict),
        status=200,
        content_type="application/json",
    )
    bugzilla = Bugsy("foo", "bar")
    bugzilla.put(bug)
    assert bug.id is not None


@responses.activate
def test_we_can_put_a_current_bug(bug_return):
    responses.add(
        responses.GET,
        "https://bugzilla.mozilla.org/rest/login",
        body='{"token": "foobar"}',
        status=200,
        content_type="application/json",
    )
    bug_dict = bug_return.copy()
    bug_dict["summary"] = "I love foo but hate bar"
    responses.add(
        responses.PUT,
        "https://bugzilla.mozilla.org/rest/bug/1017315",
        body=json.dumps(bug_dict),
        status=200,
        content_type="application/json",
    )
    responses.add(
        responses.GET,
        rest_url("bug", 1017315),
        body=json.dumps(bug_return),
        status=200,
        content_type="application/json",
    )
    bugzilla = Bugsy("foo", "bar")
    bug = Bug(**bug_return["bugs"][0])
    bug.summary = "I love foo but hate bar"
    bug.assigned_to = "automatedtester@mozilla.com"

    bugzilla.put(bug)
    assert bug.summary == "I love foo but hate bar"
    assert bug.assigned_to == "automatedtester@mozilla.com"


@responses.activate
def test_we_handle_errors_from_bugzilla_when_posting():
    responses.add(
        responses.GET,
        "https://bugzilla.mozilla.org/rest/login",
        body='{"token": "foobar"}',
        status=200,
        content_type="application/json",
    )
    responses.add(
        responses.POST,
        "https://bugzilla.mozilla.org/rest/bug",
        body='{"error":true,"code":50,"message":"You must select/enter a component."}',
        status=400,
        content_type="application/json",
    )

    bugzilla = Bugsy("foo", "bar")
    bug = Bug()
    with pytest.raises(BugsyException) as e:
        bugzilla.put(bug)
    assert str(e.value) == "Message: You must select/enter a component. Code: 50"


@responses.activate
def test_we_handle_errors_from_bugzilla_when_updating_a_bug(bug_return):
    responses.add(
        responses.GET,
        "https://bugzilla.mozilla.org/rest/login",
        body='{"token": "foobar"}',
        status=200,
        content_type="application/json",
    )
    responses.add(
        responses.PUT,
        "https://bugzilla.mozilla.org/rest/bug/1017315",
        body='{"error":true,"code":50,"message":"You must select/enter a component."}',
        status=400,
        content_type="application/json",
    )
    bugzilla = Bugsy("foo", "bar")

    bug_dict = bug_return.copy()
    bug_dict["summary"] = "I love foo but hate bar"
    bug = Bug(**bug_dict["bugs"][0])
    with pytest.raises(BugsyException) as e:
        bugzilla.put(bug)
    assert str(e.value) == "Message: You must select/enter a component. Code: 50"


@responses.activate
def test_we_can_set_the_user_agent_to_bugsy():
    responses.add(
        responses.GET,
        "https://bugzilla.mozilla.org/rest/login",
        body='{"token": "foobar"}',
        status=200,
        content_type="application/json",
    )
    Bugsy("foo", "bar")
    assert responses.calls[0].request.headers["User-Agent"] == "Bugsy"


@responses.activate
def test_we_can_handle_errors_when_retrieving_bugs():
    error_response = {
        "code": 101,
        "documentation": "http://www.bugzilla.org/docs/tip/en/html/api/",
        "error": True,
        "message": "Bug 111111111111 does not exist.",
    }
    responses.add(
        responses.GET,
        rest_url("bug", 111111111),
        body=json.dumps(error_response),
        status=404,
        content_type="application/json",
    )
    bugzilla = Bugsy()
    with pytest.raises(BugsyException) as e:
        bugzilla.get(111111111)
    assert str(e.value) == "Message: Bug 111111111111 does not exist. Code: 101"


def test_we_can_know_when_bugsy_is_not_authenticated():
    bugzilla = Bugsy()
    assert not bugzilla.authenticated


@responses.activate
def test_we_can_know_when_bugsy_is_authenticated_using_password():
    responses.add(
        responses.GET,
        "https://bugzilla.mozilla.org/rest/login",
        body='{"token": "foobar"}',
        status=200,
        content_type="application/json",
    )
    bugzilla = Bugsy("foo", "bar")
    assert bugzilla.authenticated


@responses.activate
def test_we_can_know_when_bugsy_is_authenticated_using_apikey():
    responses.add(
        responses.GET,
        "https://bugzilla.mozilla.org/rest/valid_login?login=foo",
        body="true",
        status=200,
        content_type="application/json",
    )
    bugzilla = Bugsy(username="foo", api_key="goodkey")
    assert bugzilla.authenticated
