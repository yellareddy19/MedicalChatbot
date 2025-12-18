from setuptools import find_packages, setup

def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as f:
        lines = []
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("-e "):
                continue
            lines.append(line)
        return lines

setup(
    name="medical_chatbot",
    version="0.1.0",
    author="yellareddy",
    author_email="reddy@gmail.com",
    packages=find_packages(),
    install_requires=read_requirements(),
)
