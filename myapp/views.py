from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Agent
from .serializers import AgentSerializer
import requests

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        provider = data.get("provider")

        if provider == "vapi":
            payload = {
                "name": data["agent_name"],
                "firstMessage": data.get("firstMessage"),
                
                "voice": {
                  "provider": "deepgram",
                  "voiceId": "asteria"
                  },
                  "transcriber": {
                  "provider": "assembly-ai"
                }
            }
            url = "https://api.vapi.ai/assistant"
            headers={
              "Authorization": "Bearer 1f11fa6b-85ca-45ec-a52f-796311a4ebee",
              "Content-Type": "application/json"
            }
        elif provider == "retell":
            payload = {
                "agent_name": data["agent_name"],
                "voicemail_message": data["firstMessage"],
                # "voice_type": data.get("voice", "default"),
                "response_engine": {
                "type": "retell-llm",
                "llm_id": "llm_4853aa9e76e29b00ee754224ea8b",
                "model": "gpt-4",
              },
                  "voice_id": "11labs-Adrian",
                  "voice_temperature": 1,
                "voice_speed": 1,
                "volume": 1,
                "responsiveness": 1,
                "interruption_sensitivity": 1,
                "enable_backchannel": True,
                "backchannel_frequency": 0.9,
                "backchannel_words": [
                  "yeah",
                  "uh-huh"
                ],
                "reminder_trigger_ms": 10000,
                "reminder_max_count": 2,
                "ambient_sound": "coffee-shop",
                "ambient_sound_volume": 1,
                "language": "en-US",
                "webhook_url": "https://webhook-url-here",
                "boosted_keywords": [
                  "retell",
                  "kroger"
                ],
                "enable_transcription_formatting": True,
                "opt_out_sensitive_data_storage": True,
                
                "normalize_for_speech": True,
                "end_call_after_silence_ms": 600000,
                "max_call_duration_ms": 3600000,
                "enable_voicemail_detection": True,
                "voicemail_message": "Hi, please give us a callback.",
                "voicemail_detection_timeout_ms": 30000,
                
                "post_call_analysis_model": "gpt-4o-mini",
                "begin_message_delay_ms": 1000,
                "ring_duration_ms": 30000,
                "stt_mode": "fast",
                }
           
            url = "https://api.retellai.com/create-agent"
            headers = {"Authorization": "Bearer key_8ed7350c5f7ee7e0859ca06a1980"}
        else:
            return Response({"error": "Unsupported provider."}, status=400)

        
        
        try:
            response = requests.post(url, json=payload, headers=headers)
            
            if response.status_code in [200, 201]:
                # Save to DB only if external API call is successful
                self.perform_create(serializer)
                return Response(response.json(), status=response.status_code)
            else:
                return Response({
                    "error": f"API call to {provider} failed.",
                    "details": response.json()
                }, status=response.status_code)
        except Exception as e:
            return Response({"error": str(e)}, status=500)


# # Create Assistant (POST /assistant)


# print(response.json())
