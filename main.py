from src.ticket_agent import process_ticket

def main():
    print("Single AI Agent using PydanticAI")
    print("Type exit to stop")

    while True:
        msg = input("\nCustomer Message : ")

        if msg.lower() == "exit":
            print("Good Bye!!")
            return 
        
        result = process_ticket(msg)
        print(result.model_dump_json(indent=4))

if __name__ == "__main__":
    main()
    
