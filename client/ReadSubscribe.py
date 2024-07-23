from DataBaseManager.settings_db import banco, credentialBorker
from DataBaseManager.OperationalDataBase import DataBasePostgreSQL
from clientMQTT import Main, SubscribeMQTTClient

dbPostgreSQL = DataBasePostgreSQL(banco)
subClient = SubscribeMQTTClient(
    dbPostgreSQL, credentialBorker['user'], credentialBorker['password']
)

main = Main(subClient)
main.run()
