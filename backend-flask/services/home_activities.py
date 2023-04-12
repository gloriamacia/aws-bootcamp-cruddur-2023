# from datetime import datetime, timedelta, timezoneas

from lib.db import db

# for rollbar
# import sys
# import rollbar

# # ------------Honeycomb--------
# from opentelemetry import trace

# # from opentelemetry.trace import Status, StatusCode

# tracer = trace.get_tracer("home_activites")
# @tracer.start_as_current_span("do_work")
# def do_work():
#     print("doing some work...")
# --------------------------------------


class HomeActivities:
    def run(cognito_user_id=None):
        # # for cloudwatch-watchtower
        # def run():

        # LOGGER.info('Hello Cloudwatch! from  /api/activities/home')

        # # honeycomb.io create span
        # with tracer.start_as_current_span("home-activities-mock-data"):

        # span = trace.get_current_span()
        # now = datetime.now(timezone.utc).astimezone()
        # span.set_attribute("app.now", now.isoformat())

        sql = db.template("activities", "home")
        results = db.query_array_json(sql)
        return results

        # results = [
        #     {
        #         "uuid": "68f126b0-1ceb-4a33-88be-d90fa7109eee",
        #         "handle": "Andrew Brown",
        #         "message": "Cloud is very fun!",
        #         "created_at": (now - timedelta(days=2)).isoformat(),
        #         "expires_at": (now + timedelta(days=5)).isoformat(),
        #         "likes_count": 5,
        #         "replies_count": 1,
        #         "reposts_count": 0,
        #         "replies": [
        #             {
        #                 "uuid": "26e12864-1c26-5c3a-9658-97a10f8fea67",
        #                 "reply_to_activity_uuid": "68f126b0-1ceb-4a33-88be-d90fa7109eee",
        #                 "handle": "Worf",
        #                 "message": "This post has no honor!",
        #                 "likes_count": 0,
        #                 "replies_count": 0,
        #                 "reposts_count": 0,
        #                 "created_at": (now - timedelta(days=2)).isoformat(),
        #             }
        #         ],
        #     },
        #     {
        #         "uuid": "66e12864-8c26-4c3a-9658-95a10f8fea67",
        #         "handle": "Worf",
        #         "message": "I am out of prune juice",
        #         "created_at": (now - timedelta(days=7)).isoformat(),
        #         "expires_at": (now + timedelta(days=9)).isoformat(),
        #         "likes": 0,
        #         "replies": [],
        #     },
        #     {
        #         "uuid": "248959df-3079-4947-b847-9e0892d1bab4",
        #         "handle": "Garek",
        #         "message": "My dear doctor, I am just simple tailor",
        #         "created_at": (now - timedelta(hours=1)).isoformat(),
        #         "expires_at": (now + timedelta(hours=12)).isoformat(),
        #         "likes": 0,
        #         "replies": [],
        #     },
        # ]

        # if cognito_user_id != None:
        #     extra_crud = {
        #         "uuid": "248959df-3079-4947-b847-9e0892d1baz4",
        #         "handle": "Lore",
        #         "message": "My dear brother, it the humans that are the problem",
        #         "created_at": (now - timedelta(hours=1)).isoformat(),
        #         "expires_at": (now + timedelta(hours=12)).isoformat(),
        #         "likes": 1042,
        #         "replies": [],
        #     }
        #     results.insert(0, extra_crud)

        # user = {"user": "Annlee", "userID": 123456}
        # span.set_attribute("app.result_length", len(results))

        # --- Rollbar -----

        # def ignore_handler(payload, **kw):  # kw is currently unused
        #     if payload["data"]["message"] == "test":
        #         return payload
        #     else:
        #         return False

        # rollbar.events.add_payload_handler(ignore_handler)

        # try:
        #     print(x)
        # except:

        #     payload = {
        #         "level": "error",
        #         "message": "test",
        #         "extra_data": None,  # add any extra data you want to send
        #     }

        #     rollbar.report_message(**payload)

        # return results