class Service:

    def __init__(self, name, version) -> None:
        self.name = name
        self.version = version
    
    def get_name(self) -> str:
        return self.name
    
    def set_name(self, name) -> None:
        self.name = name
    
    def get_version(self) -> int:
        return self.version
    
    def set_version(self, version) -> None:
        self.version = version
    
    def __str__(self) -> str:
        return f'Service: {self.name} | Version: {self.version}'

service = Service('Infra Service', 1)
print(service)
print('Name is:', service.get_name())
print('Version is:', service.get_version())