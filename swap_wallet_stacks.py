import os
import re

WORKSPACE = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(WORKSPACE, 'www.noth.in', 'index.html')
root_html_path = os.path.join(WORKSPACE, 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern for Brain Health stack
stack_a_pattern = r'(<!-- Fanned Cards Stack in Wallet Form -->\s*<div class="wallet-fanned-stack".*?brain_health_3\.webp.*?</div>\s*</div>)'
# Pattern for Medicine Reminder stack
stack_b_pattern = r'(<!-- Fanned Cards Stack in Wallet Form -->\s*<div class="wallet-fanned-stack".*?medicine_reminder_3\.webp.*?</div>\s*</div>)'

stack_a_match = re.search(stack_a_pattern, html, flags=re.DOTALL)
stack_b_match = re.search(stack_b_pattern, html, flags=re.DOTALL)

if stack_a_match and stack_b_match:
    stack_a_str = stack_a_match.group(1)
    stack_b_str = stack_b_match.group(1)
    
    # Placeholder swap
    PLACEHOLDER = '___SWAP_TEMP_PLACEHOLDER___'
    html = html.replace(stack_a_str, PLACEHOLDER, 1)
    html = html.replace(stack_b_str, stack_a_str, 1)
    html = html.replace(PLACEHOLDER, stack_b_str, 1)
    
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    with open(root_html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully swapped the two wallet-fanned-stack elements!")
else:
    print("Could not match one or both stacks:", bool(stack_a_match), bool(stack_b_match))
