# Density_Hackathon
## About
Problem Statement: Designing stock market auction mechanism.

Features required:
- OrderBook
- Graph
- Users portfolio
- Executed trades history
- Current Market Price
- Notifications


## Instruction
- **Create virtual environment**
```bash
sudo pip install virtualenv      # This may already be installed
virtualenv .env                  # Create a virtual environment
```
- **Activate virtual environment**
```bash
source .env/bin/activate         # Activate the virtual environment
pip install -r requirements.txt  # Check/Install dependencies
```
- **Run following commands to start backend**
```bash
./runserver.sh     # Run this bash script to start backend server
```
- **Run following commands to start frontend**
```bash
cd frontend                  # to go to frontend directory
npm i                        # to update all node modules
npm start                    # to start frontend server
```
