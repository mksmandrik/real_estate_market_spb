import vk_api
import json
import random
import requests

app_token = '0dc3a8c29818b5f1924c29966c93ff146300cfdb1ddbdf69b2f3830b08fdebf647afbcfa3a4094aec58ab'
chat_id = 1
my_id = 558437518
vk_session = vk_api.VkApi(token=app_token)
vk = vk_session.get_api()


path_to_file = '/home/jupyter-m.mandrik-1/20_3_miniproject_metrics.txt'
file_name = '20_3_miniproject_metrics.txt'

upload_url = vk.docs.getMessagesUploadServer(peer_id=my_id)["upload_url"]
file = {'file': (file_name, open(path_to_file, 'rb'))}

response = requests.post(upload_url, files=file)

json_data = json.loads(response.text)

saved_file = vk.docs.save(file=json_data['file'], title=file_name)
attachment = 'doc{}_{}'.format(saved_file['doc']['owner_id'], saved_file['doc']['id'])

vk.messages.send(
    chat_id=chat_id,
    random_id=random.randint(1, 2 ** 31),
    message='Минипроект 20-3',
    attachment=attachment)
