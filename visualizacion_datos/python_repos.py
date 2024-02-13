import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

response_dict = r.json()
print(f'Total repositores: {response_dict["total_count"]}')

repo_dicts = response_dict["items"]
print(f'Repositories returned: {len(repo_dicts)}')

# repo_dict = repo_dicts[0]

# Print keys
# print(f'\nKeys: {len(repo_dict)}')
# for key in sorted(repo_dict.keys()):
#     print(key)

print("\nSelected information about repositories")
for repo_dict in repo_dicts:
    print(f'\nName: {repo_dict["name"]}')
    print(f'Owner: {repo_dict["owner"]["login"]}')
    print(f'Stars: {repo_dict["stargazers_count"]}')
    print(f'Repository: {repo_dict["html_url"]}')
    # print(f'Created: {repo_dict["created_at"]}')
    # print(f'Updated: {repo_dict["updated_at"]}')
    print(f'Description: {repo_dict["description"]}')
