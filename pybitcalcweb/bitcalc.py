# Input validation mappings
VALID_INPUT_MAP = {
    'prefix': (
        'none',
        'kilo',
        'mega',
        'giga',
        'tera',
        'peta'
    ),
    'type': (
        'bit',
        'byte'
    ),
    'base': (
        'base-2',
        'base-10'
    )
}

# Base mappings
BASE_MAP = {
    'base-2': 1024,
    'base-10': 1000
}

# Prefix mappings
PREFIX_MAP = {
    'base-2': {
        'b': 'bit',
        'B': 'byte',
        'Kib': 'kibibit',
        'KiB': 'kibibyte',
        'Mib': 'mebibit',
        'MiB': 'mebibyte',
        'Gib': 'gibibit',
        'GiB': 'gibibyte',
        'Tib': 'tebibit',
        'TiB': 'tebibyte',
        'Pib': 'pebibit',
        'PiB': 'pebibyte',
    },
    'base-10': {
        'b': 'bit',
        'B': 'byte',
        'kb': 'kilobit',
        'kB': 'kilobyte',
        'Mb': 'megabit',
        'MB': 'megabyte',
        'Gb': 'gigabit',
        'GB': 'gigabyte',
        'Tb': 'terabit',
        'TB': 'terabyte',
        'Pb': 'petabit',
        'PB': 'petabyte'
    }
}

def sanitize_input(user_input):
    """ Checks user_input for validity

    Input: Dictionary with the following keys
        - amount: float
        - prefix: (none|kilo|mega|giga|tera|peta) (string)
        - type: (bit|byte) (string)
        - base: (base-2|base-10) (string)

    Output: Sanitized user_input dictionary
    """
    # Split out user_input keys
    amt_value = user_input['amount']
    amt_prefix = user_input['prefix'].lower()
    amt_type = user_input['type'].lower()
    amt_base = user_input['base'].lower()

    # Set up error list to track any input issues
    errors = []

    # Convert input amount to float for calculation
    try:
        amt_value = float(amt_value)
    except ValueError:
        # Append error string to errors list in user_input
        err_str = "'{}' is not a number".format(amt_value)
        errors.append(err_str)

    # Check user input against valid value lists
    valid_prefix = True if amt_prefix in VALID_INPUT_MAP['prefix'] else False
    valid_type = True if amt_type in VALID_INPUT_MAP['type'] else False
    valid_base = True if amt_base in VALID_INPUT_MAP['base'] else False

    if not valid_prefix:
        # Append error string to errors list in user_input
        err_str = "'{}' is not a valid prefix: {}".format(
            amt_prefix,
            VALID_INPUT_MAP['prefix'])
        errors.append(err_str)

    if not valid_type:
        # Append error string to errors list in user_input
        err_str = "'{}' is not a valid type: {}".format(
            amt_type,
            VALID_INPUT_MAP['type'])
        errors.append(err_str)

    if not valid_base:
        # Append error string to errors list in user_input
        err_str = "'{}' is not a valid base: {}".format(
            amt_base,
            VALID_INPUT_MAP['base'])
        errors.append(err_str)

    sanitized_input = {
        'amount': amt_value,
        'prefix': amt_prefix,
        'type': amt_type,
        'base': amt_base,
        'errors': errors
    }

    return sanitized_input


def convert_pbits_to_bits(amt_value, amt_prefix, amt_base):
    """ Convert prefixed bit value to plain bit value

    Input:
        - amt_value: Amount to convert in prefix bits (float)
        - amt_prefix: Prefix of the amount (kilo|mega|giga|tera|peta) (string)
        - amt_base: Base notation of the amount (base-2|base-10) (string)

    Output: Value in plain bits (float)
    """
    prefix_to_power = {
        'kilo': 1,
        'mega': 2,
        'giga': 3,
        'tera': 4,
        'peta': 5
    }

    return amt_value * pow(BASE_MAP[amt_base], prefix_to_power[amt_prefix])


def convert_bytes_to_bits(byte_value):
    """ Convert bytes to bits """
    return byte_value * 8


def convert_bits_to_bytes(bit_value):
    """ Convert bytes to bits """
    return bit_value / 8


def convert_amount_to_bits(amt_value, amt_prefix, amt_type, amt_base):
    """ Convert amount with prefix, type_ and base definitions to
    plain bit value

    Input:
        - amt_value: Amount bit/byte value (float)
        - amt_prefix: Prefix of the amount (kilo|mega|giga|tera|peta) (string)
        - amt_type: Type of the amount (bit|byte) (string)
        - amt_base: Base notation of the amount (base-2|base-10) (string)

    Output: Converted plain bit value
    """
    if amt_prefix == 'none' and amt_type == 'bit':
        return amt_value
    elif amt_prefix == 'none' and amt_type == 'byte':
        return convert_bytes_to_bits(amt_value)
    elif amt_type == 'byte':
        pbit_value = convert_bytes_to_bits(amt_value)
    else:
        pbit_value = amt_value

    return convert_pbits_to_bits(pbit_value, amt_prefix, amt_base)


def generate_conversion_table(bit_value, base_key):
    """ Generate conversion table based on bit_value and base notation string

    Input:
        - bit_value: Plain bit value for conversion (float)
        - base_key: Base notation used in conversion (base-2|base-10) (string)

    Output: List of dictionaries with the following keys:
        - abbr: Abbreviated prefix label (string)
        - label: Full prefix label (string)
        - result_amount: Converted amount for specified label
    """
    base_value = BASE_MAP[base_key]
    results = []

    for idx, prefix in enumerate(PREFIX_MAP[base_key]):
        abbr = prefix
        label = PREFIX_MAP[base_key][prefix]

        if idx == 0:
            # Value is already represented in bits, do not convert
            amount = bit_value
        elif idx == 1:
            # Convert type bits to type bytes
            amount = convert_bits_to_bytes(bit_value)
        else:
            # Convert previous prefix of the same type to the next prefix
            amount = results[idx - 2]['result_amount'] / base_value

        # Define result mapping
        result = {
            'abbr': abbr,
            'label': label,
            'result_amount': amount
        }

        # Append result mapping to results list
        results.append(result)

    return results
