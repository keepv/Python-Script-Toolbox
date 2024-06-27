import json
import yaml

# 读取profiles.json文件
with open('profiles.json', 'r') as file:
    profiles = json.load(file)

# Clash配置文件内容
clash_config = []

# 遍历profiles.json中的每个配置
for profile in profiles['profiles']:
    link = profile['link']
    profile_type = profile['type']
    
    # 根据类型解析链接
    if profile_type == 'vmess':
        # 解析VMess链接
        vmess_config = {
            'name': profile['name'],
            'type': 'vmess',
            'server': link.split('@')[1].split(':')[0],
            'port': link.split(':')[1].split('?')[0],
            'uuid': link.split('id=')[1].split('&')[0],
            'alterId': 0,  # 假设alterId为0
            'cipher': 'auto',  # 假设使用自动选择加密方式
            'network': 'ws',  # 假设使用WebSocket
            'ws-path': link.split('?')[1].split('&')[0].split('=')[1],
            'tls': 'true',  # 假设使用TLS
            'sni': link.split('?')[1].split('&')[1].split('=')[1],
            'skip-cert-verify': 'false',  # 假设不跳过证书验证
        }
        clash_config.append(vmess_config)
    elif profile_type == 'trojan':
        # 解析Trojan链接
        trojan_config = {
            'name': profile['name'],
            'type': 'trojan',
            'server': link.split('@')[1].split(':')[0],
            'port': link.split(':')[1],
            'password': 'auto',  # 假设密码为auto
            'network': 'ws',  # 假设使用WebSocket
            'ws-path': link.split('?')[1].split('&')[0].split('=')[1],
            'sni': link.split('?')[1].split('&')[1].split('=')[1],
            'skip-cert-verify': 'false',  # 假设不跳过证书验证
        }
        clash_config.append(trojan_config)

# 将Clash配置写入到clash-config.yaml文件
with open('clash-config.yaml', 'w') as file:
    yaml.dump(clash_config, file, default_flow_style=False, sort_keys=False)

print("Clash配置文件已生成。")