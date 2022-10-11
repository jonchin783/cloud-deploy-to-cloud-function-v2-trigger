# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#!/usr/bin/env python3
# [START functions_cloudevent_pubsub]
import base64
import functions_framework
import requests

# Triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def subscribe(cloud_event):
    #print("Hello, " + base64.b64decode(cloud_event.data["message"]["attributes"]).decode() + "!")
    seatalk_api_url = 'https://openapi.seatalk.io/webhook/group/O8fWQE76Tp2fp1cH3aaasQ'
    #print(cloud_event.data["message"]["attributes"])

    action_message = cloud_event.data["message"]["attributes"]["Action"]
    releaseId_message = cloud_event.data["message"]["attributes"]["ReleaseId"]
    rollout_message = cloud_event.data["message"]["attributes"]["Rollout"]
    targetId_message = cloud_event.data["message"]["attributes"]["TargetId"]

    #message1 = base64.b64decode(cloud_event.data["message"]["attributes"]["Action"]).decode()
    #print(message1)
    #message2 = base64.b64decode(cloud_event.data["message"]["attributes"]["DeliveryPipelineId"]).decode()

    requests.post(
        seatalk_api_url,
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
