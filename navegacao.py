import os
import googleapiclient.discovery
import arquivoCsv, aplicativo


def capturarDados(token=None):
    global infoDados
    infoDados = []
    linkPrincipal = str(aplicativo.text_box_link.get())

    try:
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = "AIzaSyByJ4leJSWCjGhm4T52fxHxoj-45NO2AQA"

        youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey= DEVELOPER_KEY)

        request = youtube.commentThreads().list(
            part="snippet,replies",
            videoId=linkPrincipal[32:],
            maxResults=100,
            pageToken=token
        )
        response = request.execute()

    except:
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = "AIzaSyByJ4leJSWCjGhm4T52fxHxoj-45NO2AQA"

        youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=DEVELOPER_KEY)

        request = youtube.commentThreads().list(
            part="snippet,replies",
            videoId=linkPrincipal,
            maxResults=100,
            pageToken=token
        )
        response = request.execute()

    dicionary = dict(response)

    lista1 = dicionary['items']

    x = 0
    elementsList = len(lista1)
    while x < elementsList:
        pos1 = lista1[x]['snippet']
        pos2 = pos1['topLevelComment']
        pos3 = pos2['snippet']
        '''nome = pos3['authorDisplayName']
        comentario = pos3['textDisplay']
        data0 = pos3['publishedAt'][:10]
        data = datetime.strptime(data0,'%Y-%m-%d').date()
        id = x'''
        infoDados.append(pos3)
        x += 1