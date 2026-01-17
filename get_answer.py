from ollama import chat
from ollama import ChatResponse
from get_text import get_text_
from time import time
start = time()
def get_answer_(model_chat:str='gemma3',content:str='')->str:
  response: ChatResponse = chat(model=model_chat, messages=[
    {
      'role': 'user',
      'content': 'У тебя собеседование. Тебе нужно отвечать кратко по делу и чтоб все было понятно. Ответь на вопрос ' + content,
    },
  ])
  return response['message']['content']
print(get_answer_(model_chat='gemma3',
  content=get_text_(model_whisper='turbo',audio_='my_quistion.mp3')))
print(time()-start)


'''model for whisper:
tiny 	39 M 	tiny.en 	tiny 	~1 GB 	~10x
base 	74 M 	base.en 	base 	~1 GB 	~7x
small 	244 M 	small.en 	small 	~2 GB 	~4x
medium 	769 M 	medium.en 	medium 	~5 GB 	~2x
large 	1550 M 	N/A 	large 	~10 GB 	1x
turbo 	809 M 	N/A 	turbo 	~6 GB 	~8x'''


'''model for ollama
Gemma 3 	1B 	815MB 	ollama run gemma3:1b
Gemma 3 	4B 	3.3GB 	ollama run gemma3
Gemma 3 	12B 	8.1GB 	ollama run gemma3:12b
Gemma 3 	27B 	17GB 	ollama run gemma3:27b
QwQ 	32B 	20GB 	ollama run qwq
DeepSeek-R1 	7B 	4.7GB 	ollama run deepseek-r1
DeepSeek-R1 	671B 	404GB 	ollama run deepseek-r1:671b
Llama 4 	109B 	67GB 	ollama run llama4:scout
Llama 4 	400B 	245GB 	ollama run llama4:maverick
Llama 3.3 	70B 	43GB 	ollama run llama3.3
Llama 3.2 	3B 	2.0GB 	ollama run llama3.2
Llama 3.2 	1B 	1.3GB 	ollama run llama3.2:1b
Llama 3.2 Vision 	11B 	7.9GB 	ollama run llama3.2-vision
Llama 3.2 Vision 	90B 	55GB 	ollama run llama3.2-vision:90b
Llama 3.1 	8B 	4.7GB 	ollama run llama3.1
Llama 3.1 	405B 	231GB 	ollama run llama3.1:405b
Phi 4 	14B 	9.1GB 	ollama run phi4
Phi 4 Mini 	3.8B 	2.5GB 	ollama run phi4-mini
Mistral 	7B 	4.1GB 	ollama run mistral
Moondream 2 	1.4B 	829MB 	ollama run moondream
Neural Chat 	7B 	4.1GB 	ollama run neural-chat
Starling 	7B 	4.1GB 	ollama run starling-lm
Code Llama 	7B 	3.8GB 	ollama run codellama
Llama 2 Uncensored 	7B 	3.8GB 	ollama run llama2-uncensored
LLaVA 	7B 	4.5GB 	ollama run llava
Granite-3.3 	8B 	4.9GB 	ollama run granite3.3'''
