echo "Cloning Repo...."
if [ -z $BRANCH ]; then
  echo "Cloning main branch...."
  git clone https://github.com/hero890/Ultra-forward-bot
else
  echo "Cloning $BRANCH branch...."
  git clone https://github.com/hero890/Ultra-forward-bot -b $BRANCH /fwdbot
fi

cd Ultra-forward-bot  # Changed directory to the cloned repository

# Ensure pip3 is installed
if ! command -v pip3 &>/dev/null; then
    echo "pip3 not found. Installing pip3..."
    sudo apt-get update
    sudo apt-get install python3-pip -y
fi

echo "Installing/updating dependencies..."
pip3 install -U -r requirements.txt

echo "Starting Bot...."
python3 main.py
