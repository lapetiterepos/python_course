def configure_intf(intf_name, ip, mask):
    print('interface', intf_name)
    print('ip address', ip, mask)

def configure_intf(intf_name, ip, mask):
    config = f'interface {intf_name}\nip address {ip} {mask}'
    return config

def configure_intf(intf_name, ip, mask):
    config = f'interface {intf_name}\nip address {ip} {mask}'
    return config
    print('Конфигурация готова')

def configure_intf(intf_name, ip, mask):
    config_intf = f'interface {intf_name}\n'
    config_ip = f'ip address {ip} {mask}'
    return config_intf, config_ip

def configure_intf(intf_name, ip, mask):
    '''
    Функция генерирует конфигурацию интерфейса
    '''
    config_intf = f'interface {intf_name}\n'
    config_ip = f'ip address {ip} {mask}'
    return config_intf, config_ip
