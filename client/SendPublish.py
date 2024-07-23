from clientMQTT import Main, PlublishMQTTClient
from DataBaseManager.settings_db import credentialBorker

pubClient = PlublishMQTTClient(
    credentialBorker['user'], credentialBorker['password']
)
main = Main(pubClient)
main.run()
