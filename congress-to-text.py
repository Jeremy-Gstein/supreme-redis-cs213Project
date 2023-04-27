import requests
from lxml import etree

# URL of the XML file to download (govinfo.gov)
# list of numbers for the N Congress (where N is the number of the Congress)

# {}'s will hold the congress_volume in main()
url = 'https://www.govinfo.gov/content/pkg/STATUTE-{}/uslm/STATUTE-{}.xml'


# formatted_url = url.format(congress_volume, congress_volume)

def parse_xml(xml_content):
    # Parse the XML content
    root = etree.fromstring(xml_content)
    # Extract text from XML using XPath
    text_elements = root.xpath('//text()')
    # Join text elements and remove unnecessary whitespace
    text = ' '.join([elem.strip() for elem in text_elements if elem.strip()])
    return text

def output_txt(text, congress_volume):
    with open(f'output{congress_volume}.txt', 'w', encoding='utf-8') as f:
        f.write(text)


def main():
    congress_volume = 1
    # Download the XML file
    while congress_volume != 200:
        try:
            formatted_url = url.format(congress_volume, congress_volume)
            response = requests.get(formatted_url)
            xml_content = response.content
            text = parse_xml(xml_content)
            output_txt(text,congress_volume)
            congress_volume += 1
        except:
            pass
        finally:
            congress_volume += 1

if __name__ == '__main__':
    main()
