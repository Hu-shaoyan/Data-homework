from github import Github

# 你的GitHub个人访问令牌
token = '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'

# 创建Github对象
g = Github(token)

user = g.get_user()

following = user.get_following()

for follower in following:
    print(f"Follower: {follower.login}")

    repos = follower.get_repos()

    for repo in repos:
        print(f"  Repo: {repo.name}")

        with open('follower_repos.txt', 'a') as file:
            file.write(f"{follower.login}/{repo.name}\n")