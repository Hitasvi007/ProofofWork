import hashlib
import time

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0  
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = str(self.timestamp) + str(self.data) + str(self.nonce) + str(self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.compute_hash()
    def format_timestamp(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.timestamp))

class Blockchain:
    def __init__(self, difficulty):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block("Genesis Block", "0")
        genesis_block.mine_block(self.difficulty)
        self.chain.append(genesis_block)

    def add_block(self, data):
        previous_hash = self.chain[-1].hash  
        new_block = Block(data, previous_hash)  
        new_block.mine_block(self.difficulty)   
        self.chain.append(new_block)           

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.compute_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def display_chain(self):
        for block in self.chain:
            print(f"Block {self.chain.index(block)}:")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Nonce: {block.nonce}")
            print(f"Hash: {block.hash}")
            print(f"Previous Hash: {block.previous_hash}\n")



if __name__ == "__main__":
    difficulty = 5  
    my_blockchain = Blockchain(difficulty)

    my_blockchain.add_block({
        "sensor_id": "WeatherStation_01",
        "location": "City_Park",
        "readings": {
            "temperature": 18.3,  
            "humidity": 70.4,     
            "wind_speed": 12.8,   
            "rainfall": 5.2      
        }
    })

    my_blockchain.add_block({
        "sensor_id": "AirMonitor_X5",
        "location": "Downtown",
        "readings": {
            "CO2": 400,           
            "PM2.5": 35,          
            "PM10": 50,          
            "Ozone": 0.07         
        }
    })

    my_blockchain.add_block({
        "sensor_id": "Machine_23",
        "location": "Factory_Floor_2",
        "readings": {
            "vibration": 0.3,     
            "temperature": 75.0,  
            "noise_level": 85,    
            "operating_hours": 120 
        },
        "timestamp": "2024-08-29 09:50:00"
    })

    my_blockchain.add_block({
        "sensor_id": "WaterSensor_Lake_1",
        "location": "Lake_Reservoir",
        "readings": {
            "pH": 7.4,           
            "dissolved_oxygen": 6.8, 
            "turbidity": 2.3,     
            "conductivity": 150   
        }
    })

    my_blockchain.add_block({
        "sensor_id": "SoilMoisture_12",
        "location": "Farm_Field_4",
        "readings": {
            "soil_moisture": 32.5, 
            "soil_temperature": 19.7, 
            "nitrogen_level": 15,  
            "phosphorus_level": 10 
        }
    })

    my_blockchain.display_chain()

    print("Is Blockchain Valid?", my_blockchain.is_chain_valid())
