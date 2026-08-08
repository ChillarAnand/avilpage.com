import csv
from urllib.parse import urlparse

# ==========================================
# CONFIGURATION
# ==========================================
# Replace these with your actual file names
CC_FILE_PATH = '/Users/anand/Downloads/cc-main-2025-aug-sep-oct-domain-vertices.txt'
SMALL_WEB_FILE_PATH = '/Users/anand/projects/smallweb/smallweb.txt'
OUTPUT_FILE_PATH = 'common_domains_found.csv'


def get_reversed_domain(url):
    """
    Parses a full URL and returns the domain in Common Crawl
    reversed format.
    Example: http://sub.example.com/feed -> com.example.sub
    """
    try:
        # Ensure url has scheme for urlparse to work correctly
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url

        parsed = urlparse(url)
        hostname = parsed.hostname

        if not hostname:
            return None

        # Split by dot and reverse the list
        parts = hostname.split('.')
        reversed_parts = parts[::-1]

        # Join back with dots (e.g., com.example.blog)
        return ".".join(reversed_parts)
    except Exception:
        return None


def unreverse_domain(reversed_domain):
    """
    Converts com.example back to example.com for readable output
    """
    if not reversed_domain:
        return ""
    return ".".join(reversed_domain.split('.')[::-1])


def main():
    print("Step 1: Loading and processing Small Web URLs...")

    # We use a set for O(1) lookup speed
    target_domains_reversed = set()

    try:
        with open(SMALL_WEB_FILE_PATH, 'r', encoding='utf-8') as f:
            for line in f:
                url = line.strip()
                if url:
                    rev_domain = get_reversed_domain(url)
                    if rev_domain:
                        target_domains_reversed.add(rev_domain)

        print(f" -> Loaded {len(target_domains_reversed)} unique domains from Small Web list.")

    except FileNotFoundError:
        print(f"Error: Could not find file {SMALL_WEB_FILE_PATH}")
        return

    print("Step 2: Streaming Common Crawl data and finding matches...")

    matches_found = 0

    try:
        with open(CC_FILE_PATH, 'r', encoding='utf-8') as cc_file, \
                open(OUTPUT_FILE_PATH, 'w', encoding='utf-8', newline='') as out_file:

            writer = csv.writer(out_file)
            writer.writerow(['Original_Format', 'Readable_Domain', 'CC_Count'])

            for line in cc_file:
                # CC Format: ID \t reversed.domain \t count
                parts = line.strip().split('\t')

                if len(parts) >= 2:
                    cc_reversed_domain = parts[1]

                    # CHECK FOR MATCH
                    # We check if the CC domain exists in our Small Web set
                    if cc_reversed_domain in target_domains_reversed:
                        count = parts[2] if len(parts) > 2 else "0"
                        readable = unreverse_domain(cc_reversed_domain)

                        # Write to file
                        writer.writerow([cc_reversed_domain, readable, count])
                        matches_found += 1

                        # Optional: Print progress every 1 million lines if file is huge
                        # if line_number % 1000000 == 0: print(...)

        print(f" -> Done! Found {matches_found} common domains.")
        print(f" -> Results saved to: {OUTPUT_FILE_PATH}")

    except FileNotFoundError:
        print(f"Error: Could not find file {CC_FILE_PATH}")


if __name__ == "__main__":
    main()