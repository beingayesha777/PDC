import Pyro4

# use name server object lookup uri shortcut
server = Pyro4.Proxy("PYRONAME:server")
print(server.welcomeMessage("anything"))
