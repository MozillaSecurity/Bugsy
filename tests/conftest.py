import pytest


@pytest.fixture(scope="module")
def bug_return():
    return {
        "faults": [],
        "bugs": [
            {
                "cf_tracking_firefox29": "---",
                "classification": "Other",
                "creator": "jgriffin@mozilla.com",
                "cf_status_firefox30": "---",
                "depends_on": [123456],
                "cf_status_firefox32": "---",
                "creation_time": "2014-05-28T23:57:58Z",
                "product": "Release Engineering",
                "cf_user_story": "",
                "dupe_of": None,
                "cf_tracking_firefox_relnote": "---",
                "keywords": ["regression"],
                "cf_tracking_b2g18": "---",
                "summary": "Schedule Mn tests on opt Linux builds on cedar",
                "id": 1017315,
                "assigned_to_detail": {
                    "id": 347295,
                    "email": "jgriffin@mozilla.com",
                    "name": "jgriffin@mozilla.com",
                    "real_name": "Jonathan Griffin (:jgriffin)",
                },
                "severity": "normal",
                "is_confirmed": True,
                "is_creator_accessible": True,
                "cf_status_b2g_1_1_hd": "---",
                "qa_contact_detail": {
                    "id": 20203,
                    "email": "catlee@mozilla.com",
                    "name": "catlee@mozilla.com",
                    "real_name": "Chris AtLee [:catlee]",
                },
                "priority": "--",
                "platform": "All",
                "cf_crash_signature": "",
                "version": "unspecified",
                "cf_qa_whiteboard": "",
                "cf_status_b2g_1_3t": "---",
                "cf_status_firefox31": "---",
                "is_open": False,
                "cf_blocking_fx": "---",
                "status": "RESOLVED",
                "cf_tracking_relnote_b2g": "---",
                "cf_status_firefox29": "---",
                "blocks": [654321],
                "qa_contact": "catlee@mozilla.com",
                "see_also": [],
                "component": "General Automation",
                "cf_tracking_firefox32": "---",
                "cf_tracking_firefox31": "---",
                "cf_tracking_firefox30": "---",
                "op_sys": "All",
                "groups": [],
                "cf_blocking_b2g": "---",
                "target_milestone": "---",
                "is_cc_accessible": True,
                "cf_tracking_firefox_esr24": "---",
                "cf_status_b2g_1_2": "---",
                "cf_status_b2g_1_3": "---",
                "cf_status_b2g18": "---",
                "cf_status_b2g_1_4": "---",
                "url": "",
                "creator_detail": {
                    "id": 347295,
                    "email": "jgriffin@mozilla.com",
                    "name": "jgriffin@mozilla.com",
                    "real_name": "Jonathan Griffin (:jgriffin)",
                },
                "whiteboard": "",
                "cf_status_b2g_2_0": "---",
                "cc_detail": [
                    {
                        "id": 30066,
                        "email": "coop@mozilla.com",
                        "name": "coop@mozilla.com",
                        "real_name": "Chris Cooper [:coop]",
                    },
                    {
                        "id": 397261,
                        "email": "dburns@mozilla.com",
                        "name": "dburns@mozilla.com",
                        "real_name": "David Burns :automatedtester",
                    },
                    {
                        "id": 438921,
                        "email": "jlund@mozilla.com",
                        "name": "jlund@mozilla.com",
                        "real_name": "Jordan Lund (:jlund)",
                    },
                    {
                        "id": 418814,
                        "email": "mdas@mozilla.com",
                        "name": "mdas@mozilla.com",
                        "real_name": "Malini Das [:mdas]",
                    },
                ],
                "alias": None,
                "cf_tracking_b2g_v1_2": "---",
                "cf_tracking_b2g_v1_3": "---",
                "flags": [],
                "assigned_to": "jgriffin@mozilla.com",
                "cf_status_firefox_esr24": "---",
                "resolution": "FIXED",
                "last_change_time": "2014-05-30T21:20:17Z",
                "cc": [
                    "coop@mozilla.com",
                    "dburns@mozilla.com",
                    "jlund@mozilla.com",
                    "mdas@mozilla.com",
                ],
                "cf_blocking_fennec": "---",
            }
        ],
    }


@pytest.fixture(scope="module")
def comments_return():
    return {
        "bugs": {
            "1017315": {
                "comments": [
                    {
                        "attachment_id": None,
                        "author": "gps@mozilla.com",
                        "bug_id": 1017315,
                        "creation_time": "2014-03-27T23:47:45Z",
                        "creator": "gps@mozilla.com",
                        "id": 8589785,
                        "is_private": False,
                        "raw_text": "raw text 1",
                        "tags": ["tag1", "tag2"],
                        "text": "text 1",
                        "time": "2014-03-27T23:47:45Z",
                    },
                    {
                        "attachment_id": 8398207,
                        "author": "gps@mozilla.com",
                        "bug_id": 1017315,
                        "creation_time": "2014-03-27T23:56:34Z",
                        "creator": "gps@mozilla.com",
                        "id": 8589812,
                        "is_private": True,
                        "raw_text": "raw text 2",
                        "tags": [],
                        "text": "text 2",
                        "time": "2014-03-27T23:56:34Z",
                    },
                ],
            },
        },
    }


@pytest.fixture(scope="module")
def attachment_return():
    return {
        "bugs": {
            "1017315": [
                {
                    "is_private": 0,
                    "creator": "abc@xyz.com",
                    "bug_id": 1017315,
                    "last_change_time": "2019-09-18T18:31:57Z",
                    "size": 0,
                    "creator_detail": {},
                    "file_name": "file1.txt",
                    "summary": "File 1 summary",
                    "creation_time": "2017-03-02T17:21:23Z",
                    "id": 8842942,
                    "is_obsolete": 0,
                    "flags": [],
                    "data": "",
                    "description": "File 2 description",
                    "content_type": "text/html",
                    "attacher": "abc@xyz.com",
                    "is_patch": 0,
                }
            ]
        }
    }
