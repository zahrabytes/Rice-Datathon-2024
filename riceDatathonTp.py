from taipy.gui import Gui
from math import cos, exp
from starknet_py.net.full_node_client import FullNodeClient
from starknet_py.net.models.chains import StarknetChainId
from starknet_py.net.signer.stark_curve_signer import KeyPair
from starknet_py.contract import Contract

content = ""
img_path = "placeholder_image.png"
prob = 0
pred = ""
chevron_path = r"Chevron_Logo.svg.png"
plots = r"plots.png"
graph1 = r"graph1.png"
graph2 = r"graph2.png"
payment_contract_address = "0x06689f1bf69af5b8e94e5ab9778c885b37c593d1156234eb423967621f596e73"

page = """
<|text-center|
### Donation to Clean Energy
<|Amount Paid|input|type=number|step=0.01|>
<|Your Address|input|type=text|>

<|Donate to Clean Energy|button|callback=on_button_press|clear_fields=Amount Paid,Your Address|>
# Rice Datathon *2024* 

<|{chevron_path}|image|>
>
<|{content}|file_selector|extensions=.csv|>
Select a CSV file from your file system.

### Prediction
<|{pred}|text|>
Prediction Probability: <|{prob}|text|>
"""

async def on_button_press(state):
    try:
        # Initialize your StarkNet client
        node_url = "https://your.starknet.node.url" 
        client = FullNodeClient(node_url=node_url)

        # Replace with the ABI of your payment smart contract
        payment_contract_abi = [...]  # Replace [...] with your actual ABI

        # Create the payment contract instance
        payment_contract = Contract(
            address=payment_contract_address,
            abi=payment_contract_abi,
            provider=client,
        )

        # Get the values from the GUI state
        amount_paid = state['Amount Paid']
        their_address = state['Your Address']

        # Use their_address as the sender key (for demonstration purposes only, not recommended for real applications)
        sender_key = their_address.encode('utf-8')  # Convert the entered address to bytes

        # Invoke the payment function
        invocation = await payment_contract.functions["pay"].invoke(sender_key, amount_paid, their_address)

        # Wait for the transaction to be accepted
        await invocation.wait_for_acceptance()

        confirmation_message = f"Donation of {amount_paid} made successfully to {their_address}. Thank you!"
        Gui.notify(confirmation_message, duration=5)  # Display a notification for 5 seconds

    except Exception as e:
        # Display a failed message
        failed_message = f"Failed to make donation: {str(e)}"
        Gui.notify(failed_message, duration=5)  # Display a notification for 5 seconds

value = 0

Gui(page).run(use_reloader=True, port=5001)

