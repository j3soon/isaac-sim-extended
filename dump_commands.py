import os
import re
import omni.kit.commands
from omni.isaac.python_app import OmniKitHelper

CONFIG = {
    "experience": f'{os.environ["EXP_PATH"]}/omni.isaac.sim.python.kit',
}
kit = OmniKitHelper(CONFIG)

with open('VERSION', 'r') as f:
    version = f.read()
docstring = '# Isaac Sim Commands\n\n'
docstring += f'Isaac Sim Version: `{version}`\n\n'

for name in omni.kit.commands.get_commands().keys():
    doc = omni.kit.commands.get_command_doc(name) + '\n\n'
    m = re.match(r'[\s\S]*Args:([\s\S]*)\n\n', doc, re.M)
    if m:
        s = m.group(0)
        ss = s.replace('\n    ', '\n- ')
        doc = doc.replace(s, ss)
    docstring += '## ' + name + '\n\n'
    docstring += doc

if not os.path.exists('isaac-sim-extended'):
    os.mkdir('isaac-sim-extended')
with open('isaac-sim-extended/commands.md', 'w') as f:
    f.write(docstring)

kit.stop()
kit.shutdown()
