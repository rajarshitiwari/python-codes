from pulser import Pulse, Sequence, Register
from pulser.devices import MockDevice
from sdk import Configuration, Endpoints, SDK
import json
# 1. Define Qubit Register
N = 6 # Qubitsperside
reg = Register.square(side=N, spacing=7, prefix="q")
# 2. Define Pulse Sequence and encode to JSON
seq = Sequence(reg, MockDevice)
seq.declare_channel(name="ch0", channel_id="rydberg_global")

seq.add(
    Pulse.ConstantPulse(
       duration=1000, # ns
       amplitude=2, # rad/us
detuning=-6, # rad/us
phase=0),
channel="ch0")

encoded_seq = seq.to_abstract_repr() # JSON file
# 3. Send encoded sequence to PASQAL Cloud Services
# Get API keys at
# https://portal.pasqal.cloud/api-keys

endpoints = Endpoints(
core="https://apis.pasqal.cloud/core",
account="https://apis.pasqal.cloud/account")

sdk = SDK(
client_id="my_client_id",
client_secret="my_client_secret",
endpoints=endpoints,)

# Configure Job
my_job = {"runs": 1000} # Number of shots
config = Configuration( # Configuration of emulator
dt=10.0,
precision="normal",
extra_config={"max-bond-dim": 100}
)
# Create batch on the Cloud service, wait until the execution completes, and get results
batch = sdk.create_batch(
encoded_seq,
device_type="EMU_TN",
jobs=[my_job],
configuration=config,
fetch_results=True,
)
res = [job.result for job in batch.jobs.values()]