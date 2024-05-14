# CATalogator

Enhancing Cheshire-Cat capabilities with metadata assignment and filtering.

[![Awesome plugin](https://custom-icon-badges.demolab.com/static/v1?label=&message=Awesome+plugin&color=000000&style=for-the-badge&logo=cheshire_cat_ai)](https://)

<img width="50%" src="https://raw.githubusercontent.com/Fede91/catalogator/main/catalogator.png">

The CATalogator Plugin is an open-source tool designed to integrate seamlessly with the Cheshire-Cat framework, enabling users to assign metadata to documents during upload and apply filters to the declarative memory to focus responses on specific documents.

## **_Very Important_**

Use this plugin with custom clients where you can change the structure of WebSocket messages sended to Cheshire-Cat.

## Getting Started

### Prerequisites

There are no prerequisites to use CATalogator Plugin.

### Installation and Configuration

#### Through Cheshire-Cat's GUI

1. Open the Cheshire-Cat Admin UI and head over to the plugins section.
2. Look for "CATalogator" plugin and choose to install it.
3. After installation, locate the "Configure" button next to CATalogator plugin in the list and click it to open the configuration sidebar.
4. Save your configurations to apply the changes.

CATalogator plugin will now be ready to use with your Cheshire-Cat projects.

## Usage

### Adding Metadata During Document Upload

Before uploading a new document, via plugin settings, you can add metadata in the following format:

```
key1: value1; key2: value2; ...
```

The plugin will set the metadata for each document accordingly.

### Applying Filters Using a Custom WebSocket Client

Users can apply filters on documents' metadata by passing the `filter_declarative_memory` property in the WebSocket message. Example:

```json
{
  "text": "Speak about Cheshire-Cat",
  "user_id": "user",
  "filter_declarative_memory": {
    "key1": "value1"
  }
}
```

The plugin will intercept these filters and apply them to the declarative memory, focusing the response only on matching documents.

**Warning:** If the user changes the filter in the same session while asking the same question, it's possible that Cheshire-Cat will give the same answer because it focuses on the history of the chat with the user.

## Support

Encountering issues or have queries about CATalogator plugin? Feel free to create an issue on the GitHub repository.

## Contributing

Contributions are warmly welcomed from the community! If you're interested in contributing, please fork the repository, commit your changes, and submit a pull request.

## License

CATalogator Plugin is made available under the MIT License, allowing you to use, modify, and distribute it as per your needs.

---

Enhance your Cheshire-Cat experience with CATalogator Plugin. Happy coding!
