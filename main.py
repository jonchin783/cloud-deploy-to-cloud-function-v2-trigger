#!/usr/bin/env python3
# [START functions_cloudevent_pubsub]
import base64
import functions_framework
import requests

# Triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def subscribe(cloud_event):
    api_url = '<your HTTPS url here>'

    action_message = cloud_event.data["message"]["attributes"]["Action"]
    releaseId_message = cloud_event.data["message"]["attributes"]["ReleaseId"]
    rollout_message = cloud_event.data["message"]["attributes"]["Rollout"]
    targetId_message = cloud_event.data["message"]["attributes"]["TargetId"]

    requests.post(
        api_url,
        json={
            "tag": "text",
            "text": {
                "content": "Cloud Deploy Approval Notifications - Action: " + action_message + " | Rollout: " + rollout_message + " | Release Id: " + releaseId_message + " | Target Env: " + targetId_message
            }
        },
        headers={"Content-Type": "application/json"}
    )
    print("Message sent")
# [END functions_cloudevent_pubsub]
