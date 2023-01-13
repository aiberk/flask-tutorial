from flask import Flask,jsonify,request
# from flask_cors import CORS

jsonData = [{
    "<!--...-->": {
        "Tag": "<!--...-->",
        "Description": "Defines a comment"
    },
    "<!DOCTYPE>": {
        "Tag": "<!DOCTYPE>",
        "Description": "Defines the document type"
    },
    "<a>": {
        "Tag": "<a>",
        "Description": "Defines a hyperlink"
    },
    "<abbr>": {
        "Tag": "<abbr>",
        "Description": "Defines an abbreviation or an acronym"
    },
    "<acronym>": {
        "Tag": "<acronym>",
        "Description": "Not supported in HTML5. Use <abbr> instead.Defines an acronym"
    },
    "<address>": {
        "Tag": "<address>",
        "Description": "Defines contact information for the author/owner of a document"
    },
    "<applet>": {
        "Tag": "<applet>",
        "Description": "Not supported in HTML5. Use <embed> or <object> instead.Defines an embedded applet"
    },
    "<area>": {
        "Tag": "<area>",
        "Description": "Defines an area inside an image map"
    },
    "<article>": {
        "Tag": "<article>",
        "Description": "Defines an article"
    },
    "<aside>": {
        "Tag": "<aside>",
        "Description": "Defines content aside from the page content"
    },
    "<audio>": {
        "Tag": "<audio>",
        "Description": "Defines embedded sound content"
    },
    "<b>": {
        "Tag": "<b>",
        "Description": "Defines bold text"
    },
    "<base>": {
        "Tag": "<base>",
        "Description": "Specifies the base URL/target for all relative URLs in a document"
    },
    "<basefont>": {
        "Tag": "<basefont>",
        "Description": "Not supported in HTML5. Use CSS instead.Specifies a default color, size, and font for all text in a document"
    },
    "<bdi>": {
        "Tag": "<bdi>",
        "Description": "Isolates a part of text that might be formatted in a different direction \nfrom other text outside it"
    },
    "<bdo>": {
        "Tag": "<bdo>",
        "Description": "Overrides the current text direction"
    },
    "<big>": {
        "Tag": "<big>",
        "Description": "Not supported in HTML5. Use CSS instead.Defines big text"
    },
    "<blockquote>": {
        "Tag": "<blockquote>",
        "Description": "Defines a section that is quoted from another source"
    },
    "<body>": {
        "Tag": "<body>",
        "Description": "Defines the document's body"
    },
    "<br>": {
        "Tag": "<br>",
        "Description": "Defines a single line break"
    },
    "<button>": {
        "Tag": "<button>",
        "Description": "Defines a clickable button"
    },
    "<canvas>": {
        "Tag": "<canvas>",
        "Description": "Used to draw graphics, on the fly, via scripting (usually JavaScript)"
    },
    "<caption>": {
        "Tag": "<caption>",
        "Description": "Defines a table caption"
    },
    "<center>": {
        "Tag": "<center>",
        "Description": "Not supported in HTML5. Use CSS instead.Defines centered text"
    },
    "<cite>": {
        "Tag": "<cite>",
        "Description": "Defines the title of a work"
    },
    "<code>": {
        "Tag": "<code>",
        "Description": "Defines a piece of computer code"
    },
    "<col>": {
        "Tag": "<col>",
        "Description": "Specifies column properties for each column within a <colgroup> element"
    },
    "<colgroup>": {
        "Tag": "<colgroup>",
        "Description": "Specifies a group of one or more columns in a table for formatting"
    },
    "<data>": {
        "Tag": "<data>",
        "Description": "Adds a machine-readable \ntranslation of a given content"
    },
    "<datalist>": {
        "Tag": "<datalist>",
        "Description": "Specifies a list of pre-defined options for input controls"
    },
    "<dd>": {
        "Tag": "<dd>",
        "Description": "Defines a description/value of a term in a description list"
    },
    "<del>": {
        "Tag": "<del>",
        "Description": "Defines text that has been deleted from a document"
    },
    "<details>": {
        "Tag": "<details>",
        "Description": "Defines additional details that the user can view or hide"
    },
    "<dfn>": {
        "Tag": "<dfn>",
        "Description": "Specifies a term that is going to be defined within the content"
    },
    "<dialog>": {
        "Tag": "<dialog>",
        "Description": "Defines a dialog box or window"
    },
    "<dir>": {
        "Tag": "<dir>",
        "Description": "Not supported in HTML5. Use <ul> instead.Defines a directory list"
    },
    "<div>": {
        "Tag": "<div>",
        "Description": "Defines a section in a document"
    },
    "<dl>": {
        "Tag": "<dl>",
        "Description": "Defines a description list"
    },
    "<dt>": {
        "Tag": "<dt>",
        "Description": "Defines a term/name in a description list"
    },
    "<em>": {
        "Tag": "<em>",
        "Description": "Defines emphasized text"
    },
    "<embed>": {
        "Tag": "<embed>",
        "Description": "Defines a container for an external application"
    },
    "<fieldset>": {
        "Tag": "<fieldset>",
        "Description": "Groups related elements in a form"
    },
    "<figcaption>": {
        "Tag": "<figcaption>",
        "Description": "Defines a caption for a <figure> element"
    },
    "<figure>": {
        "Tag": "<figure>",
        "Description": "Specifies self-contained content"
    },
    "<font>": {
        "Tag": "<font>",
        "Description": "Not supported in HTML5. Use CSS instead.Defines font, color, and size for text"
    },
    "<footer>": {
        "Tag": "<footer>",
        "Description": "Defines a footer for a document or section"
    },
    "<form>": {
        "Tag": "<form>",
        "Description": "Defines an HTML form for user input"
    },
    "<frame>": {
        "Tag": "<frame>",
        "Description": "Not supported in HTML5.Defines a window (a frame) in a frameset"
    },
    "<frameset>": {
        "Tag": "<frameset>",
        "Description": "Not supported in HTML5.Defines a set of frames"
    },
    "<h1> to <h6>": {
        "Tag": "<h1> to <h6>",
        "Description": "Defines HTML headings"
    },
    "<head>": {
        "Tag": "<head>",
        "Description": "Contains metadata/information for the document"
    },
    "<header>": {
        "Tag": "<header>",
        "Description": "Defines a header for a document or section"
    },
    "<hr>": {
        "Tag": "<hr>",
        "Description": "Defines a thematic change in the content"
    },
    "<html>": {
        "Tag": "<html>",
        "Description": "Defines the root of an HTML document"
    },
    "<i>": {
        "Tag": "<i>",
        "Description": "Defines a part of text in an alternate voice or mood"
    },
    "<iframe>": {
        "Tag": "<iframe>",
        "Description": "Defines an inline frame"
    },
    "<img>": {
        "Tag": "<img>",
        "Description": "Defines an image"
    },
    "<input>": {
        "Tag": "<input>",
        "Description": "Defines an input control"
    },
    "<ins>": {
        "Tag": "<ins>",
        "Description": "Defines a text that has been inserted into a document"
    },
    "<kbd>": {
        "Tag": "<kbd>",
        "Description": "Defines keyboard input"
    },
    "<label>": {
        "Tag": "<label>",
        "Description": "Defines a label\u00a0for an <input> element"
    },
    "<legend>": {
        "Tag": "<legend>",
        "Description": "Defines a caption for a <fieldset> element"
    },
    "<li>": {
        "Tag": "<li>",
        "Description": "Defines a list item"
    },
    "<link>": {
        "Tag": "<link>",
        "Description": "Defines the relationship between a document and an external resource (most \nused to link to style sheets)"
    },
    "<main>": {
        "Tag": "<main>",
        "Description": "Specifies the main content of a document"
    },
    "<map>": {
        "Tag": "<map>",
        "Description": "Defines an image map"
    },
    "<mark>": {
        "Tag": "<mark>",
        "Description": "Defines marked/highlighted text"
    },
    "<meta>": {
        "Tag": "<meta>",
        "Description": "Defines metadata about an HTML document"
    },
    "<meter>": {
        "Tag": "<meter>",
        "Description": "Defines a scalar measurement within a known range (a gauge)"
    },
    "<nav>": {
        "Tag": "<nav>",
        "Description": "Defines navigation links"
    },
    "<noframes>": {
        "Tag": "<noframes>",
        "Description": "Not supported in HTML5.Defines an alternate content for users that do not support frames"
    },
    "<noscript>": {
        "Tag": "<noscript>",
        "Description": "Defines an alternate content for users that do not support \nclient-side scripts"
    },
    "<object>": {
        "Tag": "<object>",
        "Description": "Defines a container for an external application"
    },
    "<ol>": {
        "Tag": "<ol>",
        "Description": "Defines an ordered list"
    },
    "<optgroup>": {
        "Tag": "<optgroup>",
        "Description": "Defines a group of related options in a drop-down list"
    },
    "<option>": {
        "Tag": "<option>",
        "Description": "Defines an option in a drop-down list"
    },
    "<output>": {
        "Tag": "<output>",
        "Description": "Defines the result of a calculation"
    },
    "<p>": {
        "Tag": "<p>",
        "Description": "Defines a paragraph"
    },
    "<param>": {
        "Tag": "<param>",
        "Description": "Defines a parameter for an object"
    },
    "<picture>": {
        "Tag": "<picture>",
        "Description": "Defines a container for multiple image resources"
    },
    "<pre>": {
        "Tag": "<pre>",
        "Description": "Defines preformatted text"
    },
    "<progress>": {
        "Tag": "<progress>",
        "Description": "Represents the progress of a task"
    },
    "<q>": {
        "Tag": "<q>",
        "Description": "Defines a short quotation"
    },
    "<rp>": {
        "Tag": "<rp>",
        "Description": "Defines what to show in browsers that do not support ruby annotations"
    },
    "<rt>": {
        "Tag": "<rt>",
        "Description": "Defines an explanation/pronunciation of characters (for East Asian \ntypography)"
    },
    "<ruby>": {
        "Tag": "<ruby>",
        "Description": "Defines a ruby annotation (for East Asian typography)"
    },
    "<s>": {
        "Tag": "<s>",
        "Description": "Defines text that is no longer correct"
    },
    "<samp>": {
        "Tag": "<samp>",
        "Description": "Defines sample output from a computer program"
    },
    "<script>": {
        "Tag": "<script>",
        "Description": "Defines a client-side script"
    },
    "<section>": {
        "Tag": "<section>",
        "Description": "Defines a section in a document"
    },
    "<select>": {
        "Tag": "<select>",
        "Description": "Defines a drop-down list"
    },
    "<small>": {
        "Tag": "<small>",
        "Description": "Defines smaller text"
    },
    "<source>": {
        "Tag": "<source>",
        "Description": "Defines multiple media resources for media elements (<video> and <audio>)"
    },
    "<span>": {
        "Tag": "<span>",
        "Description": "Defines a section in a document"
    },
    "<strike>": {
        "Tag": "<strike>",
        "Description": "Not supported in HTML5. Use <del> or <s> instead.Defines strikethrough text"
    },
    "<strong>": {
        "Tag": "<strong>",
        "Description": "Defines important text"
    },
    "<style>": {
        "Tag": "<style>",
        "Description": "Defines style information for a document"
    },
    "<sub>": {
        "Tag": "<sub>",
        "Description": "Defines subscripted text"
    },
    "<summary>": {
        "Tag": "<summary>",
        "Description": "Defines a visible heading for a <details> element"
    },
    "<sup>": {
        "Tag": "<sup>",
        "Description": "Defines superscripted text"
    },
    "<svg>": {
        "Tag": "<svg>",
        "Description": "Defines a container for SVG graphics"
    },
    "<table>": {
        "Tag": "<table>",
        "Description": "Defines a table"
    },
    "<tbody>": {
        "Tag": "<tbody>",
        "Description": "Groups the body content in a table"
    },
    "<td>": {
        "Tag": "<td>",
        "Description": "Defines a cell in a table"
    },
    "<template>": {
        "Tag": "<template>",
        "Description": "Defines a container for content that should be hidden when the page loads"
    },
    "<textarea>": {
        "Tag": "<textarea>",
        "Description": "Defines a multiline input control (text area)"
    },
    "<tfoot>": {
        "Tag": "<tfoot>",
        "Description": "Groups the footer content in a table"
    },
    "<th>": {
        "Tag": "<th>",
        "Description": "Defines a header cell in a table"
    },
    "<thead>": {
        "Tag": "<thead>",
        "Description": "Groups the header content in a table"
    },
    "<time>": {
        "Tag": "<time>",
        "Description": "Defines a specific time (or datetime)"
    },
    "<title>": {
        "Tag": "<title>",
        "Description": "Defines a title for the document"
    },
    "<tr>": {
        "Tag": "<tr>",
        "Description": "Defines a row in a table"
    },
    "<track>": {
        "Tag": "<track>",
        "Description": "Defines text tracks for media elements (<video> and <audio>)"
    },
    "<tt>": {
        "Tag": "<tt>",
        "Description": "Not supported in HTML5. Use CSS instead.Defines teletype text"
    },
    "<u>": {
        "Tag": "<u>",
        "Description": "Defines some text that is unarticulated and styled differently from normal \ntext"
    },
    "<ul>": {
        "Tag": "<ul>",
        "Description": "Defines an unordered list"
    },
    "<var>": {
        "Tag": "<var>",
        "Description": "Defines a variable"
    },
    "<video>": {
        "Tag": "<video>",
        "Description": "Defines embedded video content"
    },
    "<wbr>": {
        "Tag": "<wbr>",
        "Description": "Defines a possible line-break"
    }
}]

jsonData2 = [
    {
        "Attribute": "accept",
        "Belongs to": "<input>",
        "Description": "Specifies the types of files that the server accepts (only for type=\"file\")"
    },
    {
        "Attribute": "accept-charset",
        "Belongs to": "<form>",
        "Description": "Specifies the character encodings that are to be used for the form \nsubmission"
    },
    {
        "Attribute": "accesskey",
        "Belongs to": "Global Attributes",
        "Description": "Specifies a shortcut key to activate/focus an element"
    },
    {
        "Attribute": "action",
        "Belongs to": "<form>",
        "Description": "Specifies where to send the form-data when a form is submitted"
    },
    {
        "Attribute": "align",
        "Belongs to": "Not supported in HTML 5.",
        "Description": "Specifies the alignment according to surrounding elements. Use CSS instead"
    },
    {
        "Attribute": "alt",
        "Belongs to": "<area>, <img>, <input>",
        "Description": "Specifies an alternate text when the original element fails to display"
    },
    {
        "Attribute": "async",
        "Belongs to": "<script>",
        "Description": "Specifies that the script is executed asynchronously (only for external \nscripts)"
    },
    {
        "Attribute": "autocomplete",
        "Belongs to": "<form>, <input>",
        "Description": "Specifies whether the <form> or the <input> element should have autocomplete \nenabled"
    },
    {
        "Attribute": "autofocus",
        "Belongs to": "<button>, <input>, <select>, <textarea>",
        "Description": "Specifies that the element should automatically get focus when the page \nloads"
    },
    {
        "Attribute": "autoplay",
        "Belongs to": "<audio>, <video>",
        "Description": "Specifies that the audio/video will start playing as soon as it is ready"
    },
    {
        "Attribute": "bgcolor",
        "Belongs to": "Not supported in HTML 5.",
        "Description": "Specifies the background color of an element. Use CSS instead"
    },
    {
        "Attribute": "border",
        "Belongs to": "Not supported in HTML 5.",
        "Description": "Specifies the width of the border of an element. Use CSS instead"
    },
    {
        "Attribute": "charset",
        "Belongs to": "<meta>, <script>",
        "Description": "Specifies the character encoding"
    },
    {
        "Attribute": "checked",
        "Belongs to": "<input>",
        "Description": "Specifies that an <input> element should be pre-selected when the page loads \n(for type=\"checkbox\" or type=\"radio\")"
    },
    {
        "Attribute": "cite",
        "Belongs to": "<blockquote>, <del>, <ins>, <q>",
        "Description": "Specifies a URL which explains the quote/deleted/inserted text"
    },
    {
        "Attribute": "class",
        "Belongs to": "Global Attributes",
        "Description": "Specifies one or more classnames for an element (refers to a class in a \nstyle sheet)"
    },
    {
        "Attribute": "color",
        "Belongs to": "Not supported in HTML 5.",
        "Description": "Specifies the text color of an element. Use CSS instead"
    },
    {
        "Attribute": "cols",
        "Belongs to": "<textarea>",
        "Description": "Specifies the visible width of a text area"
    },
    {
        "Attribute": "colspan",
        "Belongs to": "<td>, <th>",
        "Description": "Specifies the number of columns a table cell should span"
    },
    {
        "Attribute": "content",
        "Belongs to": "<meta>",
        "Description": "Gives the value associated with the http-equiv or name attribute"
    },
    {
        "Attribute": "contenteditable",
        "Belongs to": "Global Attributes",
        "Description": "Specifies whether the content of an element is editable or not"
    },
    {
        "Attribute": "controls",
        "Belongs to": "<audio>, <video>",
        "Description": "Specifies that audio/video controls should be displayed (such as a \nplay/pause button etc)"
    },
    {
        "Attribute": "coords",
        "Belongs to": "<area>",
        "Description": "Specifies the coordinates of the area"
    },
    {
        "Attribute": "data",
        "Belongs to": "<object>",
        "Description": "Specifies the URL of the resource to be used by the object"
    },
    {
        "Attribute": "data-*",
        "Belongs to": "Global Attributes",
        "Description": "Used to store custom data private to the page or application"
    },
    {
        "Attribute": "datetime",
        "Belongs to": "<del>, <ins>, <time>",
        "Description": "Specifies the date and time"
    },
    {
        "Attribute": "default",
        "Belongs to": "<track>",
        "Description": "Specifies that the track is to be enabled if the user's preferences do not \nindicate that another track would be more appropriate"
    },
    {
        "Attribute": "defer",
        "Belongs to": "<script>",
        "Description": "Specifies that the script is executed when the page has finished parsing \n(only for external scripts)"
    },
    {
        "Attribute": "dir",
        "Belongs to": "Global Attributes",
        "Description": "Specifies the text direction for the content in an element"
    },
    {
        "Attribute": "dirname",
        "Belongs to": "<input>, <textarea>",
        "Description": "Specifies that the text direction will be submitted"
    },
    {
        "Attribute": "disabled",
        "Belongs to": "<button>, <fieldset>, <input>, <optgroup>, <option>, <select>, \n<textarea>",
        "Description": "Specifies that the specified element/group of elements should be disabled"
    },
    {
        "Attribute": "download",
        "Belongs to": "<a>, <area>",
        "Description": "Specifies that the target will be downloaded when a user clicks on the \nhyperlink"
    },
    {
        "Attribute": "draggable",
        "Belongs to": "Global Attributes",
        "Description": "Specifies whether an element is draggable or not"
    },
    {
        "Attribute": "enctype",
        "Belongs to": "<form>",
        "Description": "Specifies how the form-data should be encoded when submitting it to the \nserver (only for method=\"post\")"
    },
    {
        "Attribute": "for",
        "Belongs to": "<label>, <output>",
        "Description": "Specifies which form element(s) a label/calculation is bound to"
    },
    {
        "Attribute": "form",
        "Belongs to": "<button>, <fieldset>, <input>, <label>, <meter>, <object>, \n<output>, <select>, <textarea>",
        "Description": "Specifies the name of the form the element belongs to"
    },
    {
        "Attribute": "formaction",
        "Belongs to": "<button>, <input>",
        "Description": "Specifies where to send the form-data when a form is submitted. Only for \ntype=\"submit\""
    },
    {
        "Attribute": "headers",
        "Belongs to": "<td>, <th>",
        "Description": "Specifies one or more headers cells a cell is related to"
    },
    {
        "Attribute": "height",
        "Belongs to": "<canvas>, <embed>, <iframe>, <img>, <input>, <object>, <video>",
        "Description": "Specifies the height of the element"
    },
    {
        "Attribute": "hidden",
        "Belongs to": "Global Attributes",
        "Description": "Specifies that an element is not yet, or is no longer, relevant"
    },
    {
        "Attribute": "high",
        "Belongs to": "<meter>",
        "Description": "Specifies the range that is considered to be a high value"
    },
    {
        "Attribute": "href",
        "Belongs to": "<a>, <area>, <base>, <link>",
        "Description": "Specifies the URL of the page the link goes to"
    },
    {
        "Attribute": "hreflang",
        "Belongs to": "<a>, <area>, <link>",
        "Description": "Specifies the language of the linked document"
    },
    {
        "Attribute": "http-equiv",
        "Belongs to": "<meta>",
        "Description": "Provides an HTTP header for the information/value of the content attribute"
    },
    {
        "Attribute": "id",
        "Belongs to": "Global Attributes",
        "Description": "Specifies a unique id for an element"
    },
    {
        "Attribute": "ismap",
        "Belongs to": "<img>",
        "Description": "Specifies an image as a server-side image map"
    },
    {
        "Attribute": "kind",
        "Belongs to": "<track>",
        "Description": "Specifies the kind of text track"
    },
    {
        "Attribute": "label",
        "Belongs to": "<track>, <option>, <optgroup>",
        "Description": "Specifies the title of the text track"
    },
    {
        "Attribute": "lang",
        "Belongs to": "Global Attributes",
        "Description": "Specifies the language of the element's content"
    },
    {
        "Attribute": "list",
        "Belongs to": "<input>",
        "Description": "Refers to a <datalist> element that contains pre-defined options for an <input> \nelement"
    },
    {
        "Attribute": "loop",
        "Belongs to": "<audio>, <video>",
        "Description": "Specifies that the audio/video will start over again, every time it is \nfinished"
    },
    {
        "Attribute": "low",
        "Belongs to": "<meter>",
        "Description": "Specifies the range that is considered to be a low value"
    },
    {
        "Attribute": "max",
        "Belongs to": "<input>, <meter>, <progress>",
        "Description": "Specifies the maximum value"
    },
    {
        "Attribute": "maxlength",
        "Belongs to": "<input>, <textarea>",
        "Description": "Specifies the maximum number of characters allowed in an element"
    },
    {
        "Attribute": "media",
        "Belongs to": "<a>, <area>, <link>, <source>, <style>",
        "Description": "Specifies what media/device the linked document is optimized for"
    },
    {
        "Attribute": "method",
        "Belongs to": "<form>",
        "Description": "Specifies the HTTP method to use when sending form-data"
    },
    {
        "Attribute": "min",
        "Belongs to": "<input>, <meter>",
        "Description": "Specifies a minimum value"
    },
    {
        "Attribute": "multiple",
        "Belongs to": "<input>, <select>",
        "Description": "Specifies that a user can enter more than one value"
    },
    {
        "Attribute": "muted",
        "Belongs to": "<video>, <audio>",
        "Description": "Specifies that the audio output of the video should be muted"
    },
    {
        "Attribute": "name",
        "Belongs to": "<button>, <fieldset>, <form>, <iframe>, <input>, <map>, <meta>, \n<object>, <output>, <param>, <select>, <textarea>",
        "Description": "Specifies the name of the element"
    },
    {
        "Attribute": "novalidate",
        "Belongs to": "<form>",
        "Description": "Specifies that the form should not be validated when submitted"
    },
    {
        "Attribute": "onabort",
        "Belongs to": "<audio>, <embed>, <img>, <object>, <video>",
        "Description": "Script to be run on abort"
    },
    {
        "Attribute": "onafterprint",
        "Belongs to": "<body>",
        "Description": "Script to be run after the document is printed"
    },
    {
        "Attribute": "onbeforeprint",
        "Belongs to": "<body>",
        "Description": "Script to be run before the document is printed"
    },
    {
        "Attribute": "onbeforeunload",
        "Belongs to": "<body>",
        "Description": "Script to be run when the document is about to be unloaded"
    },
    {
        "Attribute": "onblur",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when the element loses focus"
    },
    {
        "Attribute": "oncanplay",
        "Belongs to": "<audio>, <embed>, <object>, <video>",
        "Description": "Script to be run when a file is ready to start playing (when it has buffered \nenough to begin)"
    },
    {
        "Attribute": "oncanplaythrough",
        "Belongs to": "<audio>, <video>",
        "Description": "Script to be run when a file can be played all the way to the end without \npausing for buffering"
    },
    {
        "Attribute": "onchange",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when the value of the element is changed"
    },
    {
        "Attribute": "onclick",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when the element is being clicked"
    },
    {
        "Attribute": "oncontextmenu",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when a context menu is triggered"
    },
    {
        "Attribute": "oncopy",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when the content of the element is being copied"
    },
    {
        "Attribute": "oncuechange",
        "Belongs to": "<track>",
        "Description": "Script to be run when the cue changes in a <track> element"
    },
    {
        "Attribute": "oncut",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when the content of the element is being cut"
    },
    {
        "Attribute": "ondblclick",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when the element is being double-clicked"
    },
    {
        "Attribute": "ondrag",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when the element is being dragged"
    },
    {
        "Attribute": "ondragend",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run at the end of a drag operation"
    },
    {
        "Attribute": "ondragenter",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when an element has been dragged to a valid drop target"
    },
    {
        "Attribute": "ondragleave",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when an element leaves a valid drop target"
    },
    {
        "Attribute": "ondragover",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when an element is being dragged over a valid drop target"
    },
    {
        "Attribute": "ondragstart",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run at the start of a drag operation"
    },
    {
        "Attribute": "ondrop",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when dragged element is being dropped"
    },
    {
        "Attribute": "ondurationchange",
        "Belongs to": "<audio>, <video>",
        "Description": "Script to be run when the length of the media changes"
    },
    {
        "Attribute": "onemptied",
        "Belongs to": "<audio>, <video>",
        "Description": "Script to be run when something bad happens and the file is suddenly \nunavailable (like unexpectedly disconnects)"
    },
    {
        "Attribute": "onended",
        "Belongs to": "<audio>, <video>",
        "Description": "Script to be run when the media has reach the end (a useful event for \nmessages like \"thanks for listening\")"
    },
    {
        "Attribute": "onerror",
        "Belongs to": "<audio>, <body>, <embed>, <img>, <object>, <script>, <style>, <video>",
        "Description": "Script to be run when an error occurs"
    },
    {
        "Attribute": "onfocus",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when the element gets focus"
    },
    {
        "Attribute": "onhashchange",
        "Belongs to": "<body>",
        "Description": "Script to be run when there has been changes to the anchor part of the a URL"
    },
    {
        "Attribute": "oninput",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when the element gets user input"
    },
    {
        "Attribute": "oninvalid",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when the element is invalid"
    },
    {
        "Attribute": "onkeydown",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when a user is pressing a key"
    },
    {
        "Attribute": "onkeypress",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when a user presses a key"
    },
    {
        "Attribute": "onkeyup",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when a user releases a key"
    },
    {
        "Attribute": "onload",
        "Belongs to": "<body>, <iframe>, <img>, <input>, <link>, <script>, <style>",
        "Description": "Script to be run when the element is finished loading"
    },
    {
        "Attribute": "onloadeddata",
        "Belongs to": "<audio>, <video>",
        "Description": "Script to be run when media data is loaded"
    },
    {
        "Attribute": "onloadedmetadata",
        "Belongs to": "<audio>, <video>",
        "Description": "Script to be run when meta data (like dimensions and duration) are loaded"
    },
    {
        "Attribute": "onloadstart",
        "Belongs to": "<audio>, <video>",
        "Description": "Script to be run just as the file begins to load before anything is actually \nloaded"
    },
    {
        "Attribute": "onmousedown",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when a mouse button is pressed down on an element"
    },
    {
        "Attribute": "onmousemove",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run as long as the\u00a0 mouse pointer is moving over an element"
    },
    {
        "Attribute": "onmouseout",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when a mouse pointer moves out of an element"
    },
    {
        "Attribute": "onmouseover",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when a mouse pointer moves over an element"
    },
    {
        "Attribute": "onmouseup",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when a mouse button is released over an element"
    },
    {
        "Attribute": "onmousewheel",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when a mouse wheel is being scrolled over an element"
    },
    {
        "Attribute": "onoffline",
        "Belongs to": "<body>",
        "Description": "Script to be run when the browser starts to work offline"
    },
    {
        "Attribute": "ononline",
        "Belongs to": "<body>",
        "Description": "Script to be run when the browser starts to work online"
    },
    {
        "Attribute": "onpagehide",
        "Belongs to": "<body>",
        "Description": "Script to be run when a user navigates away from a page"
    },
    {
        "Attribute": "onpageshow",
        "Belongs to": "<body>",
        "Description": "Script to be run when a user navigates to a page"
    },
    {
        "Attribute": "onpaste",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when the user pastes some content in an element"
    },
    {
        "Attribute": "onpause",
        "Belongs to": "<audio>, <video>",
        "Description": "Script to be run when the media is paused either by the user or \nprogrammatically"
    },
    {
        "Attribute": "onplay",
        "Belongs to": "<audio>, <video>",
        "Description": "Script to be run when the media has started playing"
    },
    {
        "Attribute": "onplaying",
        "Belongs to": "<audio>, <video>",
        "Description": "Script to be run when the media has started playing"
    },
    {
        "Attribute": "onpopstate",
        "Belongs to": "<body>",
        "Description": "Script to be run when the window's history changes."
    },
    {
        "Attribute": "onprogress",
        "Belongs to": "<audio>, <video>",
        "Description": "Script to be run when the browser is in the process of getting the media \ndata"
    },
    {
        "Attribute": "onratechange",
        "Belongs to": "<audio>, <video>",
        "Description": "Script to be run each time the playback rate changes (like when a user \nswitches to a slow motion or fast forward mode)."
    },
    {
        "Attribute": "onreset",
        "Belongs to": "<form>",
        "Description": "Script to be run when a reset button in a form is clicked."
    },
    {
        "Attribute": "onresize",
        "Belongs to": "<body>",
        "Description": "Script to be run when the browser window is being resized."
    },
    {
        "Attribute": "onscroll",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when an element's scrollbar is being scrolled"
    },
    {
        "Attribute": "onsearch",
        "Belongs to": "<input>",
        "Description": "Script to be run when the user writes something in a search field (for \n<input type=\"search\">)"
    },
    {
        "Attribute": "onseeked",
        "Belongs to": "<audio>, <video>",
        "Description": "Script to be run when the seeking attribute is set to false indicating that \nseeking has ended"
    },
    {
        "Attribute": "onseeking",
        "Belongs to": "<audio>, <video>",
        "Description": "Script to be run when the seeking attribute is set to true indicating that \nseeking is active"
    },
    {
        "Attribute": "onselect",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when the element gets selected"
    },
    {
        "Attribute": "onstalled",
        "Belongs to": "<audio>, <video>",
        "Description": "Script to be run when the browser is unable to fetch the media data for \nwhatever reason"
    },
    {
        "Attribute": "onstorage",
        "Belongs to": "<body>",
        "Description": "Script to be run when a Web Storage area is updated"
    },
    {
        "Attribute": "onsubmit",
        "Belongs to": "<form>",
        "Description": "Script to be run when a form is submitted"
    },
    {
        "Attribute": "onsuspend",
        "Belongs to": "<audio>, <video>",
        "Description": "Script to be run when fetching the media data is stopped before it is \ncompletely loaded for whatever reason"
    },
    {
        "Attribute": "ontimeupdate",
        "Belongs to": "<audio>, <video>",
        "Description": "Script to be run when the playing position has changed (like when the user \nfast forwards to a different point in the media)"
    },
    {
        "Attribute": "ontoggle",
        "Belongs to": "<details>",
        "Description": "Script to be run when the user opens or closes the <details> element"
    },
    {
        "Attribute": "onunload",
        "Belongs to": "<body>",
        "Description": "Script to be run when a page has unloaded (or the browser window has been \nclosed)"
    },
    {
        "Attribute": "onvolumechange",
        "Belongs to": "<audio>, <video>",
        "Description": "Script to be run each time the volume of a video/audio has been changed"
    },
    {
        "Attribute": "onwaiting",
        "Belongs to": "<audio>, <video>",
        "Description": "Script to be run when the media has paused but is expected to resume (like \nwhen the media pauses to buffer more data)"
    },
    {
        "Attribute": "onwheel",
        "Belongs to": "All visible elements.",
        "Description": "Script to be run when the mouse wheel rolls up or down over an element"
    },
    {
        "Attribute": "open",
        "Belongs to": "<details>",
        "Description": "Specifies that the details should be visible (open) to the user"
    },
    {
        "Attribute": "optimum",
        "Belongs to": "<meter>",
        "Description": "Specifies what value is the optimal value for the gauge"
    },
    {
        "Attribute": "pattern",
        "Belongs to": "<input>",
        "Description": "Specifies a regular expression that an <input> element's value is checked \nagainst"
    },
    {
        "Attribute": "placeholder",
        "Belongs to": "<input>, <textarea>",
        "Description": "Specifies a short hint that describes the expected value of the element"
    },
    {
        "Attribute": "poster",
        "Belongs to": "<video>",
        "Description": "Specifies an image to be shown while the video is downloading, or until the \nuser hits the play button"
    },
    {
        "Attribute": "preload",
        "Belongs to": "<audio>, <video>",
        "Description": "Specifies if and how the author thinks the audio/video should be loaded when \nthe page loads"
    },
    {
        "Attribute": "readonly",
        "Belongs to": "<input>, <textarea>",
        "Description": "Specifies that the element is read-only"
    },
    {
        "Attribute": "rel",
        "Belongs to": "<a>, <area>, \n<form>, <link>",
        "Description": "Specifies the relationship between the current document and the linked \ndocument"
    },
    {
        "Attribute": "required",
        "Belongs to": "<input>, <select>, <textarea>",
        "Description": "Specifies that the element must be filled out before submitting the form"
    },
    {
        "Attribute": "reversed",
        "Belongs to": "<ol>",
        "Description": "Specifies that the list order should be descending (9,8,7...)"
    },
    {
        "Attribute": "rows",
        "Belongs to": "<textarea>",
        "Description": "Specifies the visible number of lines in a text area"
    },
    {
        "Attribute": "rowspan",
        "Belongs to": "<td>, <th>",
        "Description": "Specifies the number of rows a table cell should span"
    },
    {
        "Attribute": "sandbox",
        "Belongs to": "<iframe>",
        "Description": "Enables an extra set of restrictions for the content in an <iframe>"
    },
    {
        "Attribute": "scope",
        "Belongs to": "<th>",
        "Description": "Specifies whether a header cell is a header for a column, row, or group of \ncolumns or rows"
    },
    {
        "Attribute": "selected",
        "Belongs to": "<option>",
        "Description": "Specifies that an option should be pre-selected when the page loads"
    },
    {
        "Attribute": "shape",
        "Belongs to": "<area>",
        "Description": "Specifies the shape of the area"
    },
    {
        "Attribute": "size",
        "Belongs to": "<input>, <select>",
        "Description": "Specifies the width, in characters (for <input>) or specifies the number of \nvisible options (for <select>)"
    },
    {
        "Attribute": "sizes",
        "Belongs to": "<img>, <link>,\n<source>",
        "Description": "Specifies the size of the linked resource"
    },
    {
        "Attribute": "span",
        "Belongs to": "<col>, <colgroup>",
        "Description": "Specifies the number of columns to span"
    },
    {
        "Attribute": "spellcheck",
        "Belongs to": "Global Attributes",
        "Description": "Specifies whether the element is to have its spelling and grammar checked or \nnot"
    },
    {
        "Attribute": "src",
        "Belongs to": "<audio>, <embed>, <iframe>, <img>, <input>, <script>, <source>, <track>, \n<video>",
        "Description": "Specifies the URL of the media file"
    },
    {
        "Attribute": "srcdoc",
        "Belongs to": "<iframe>",
        "Description": "Specifies the HTML content of the page to show in the <iframe>"
    },
    {
        "Attribute": "srclang",
        "Belongs to": "<track>",
        "Description": "Specifies the language of the track text data (required if kind=\"subtitles\")"
    },
    {
        "Attribute": "srcset",
        "Belongs to": "<img>, <source>",
        "Description": "Specifies the URL of the image to use in different situations"
    },
    {
        "Attribute": "start",
        "Belongs to": "<ol>",
        "Description": "Specifies the start value of an ordered list"
    },
    {
        "Attribute": "step",
        "Belongs to": "<input>",
        "Description": "Specifies the legal number intervals for an input field"
    },
    {
        "Attribute": "style",
        "Belongs to": "Global Attributes",
        "Description": "Specifies an inline CSS style for an element"
    },
    {
        "Attribute": "tabindex",
        "Belongs to": "Global Attributes",
        "Description": "Specifies the tabbing order of an element"
    },
    {
        "Attribute": "target",
        "Belongs to": "<a>, <area>, <base>, <form>",
        "Description": "Specifies the target for where to open the linked document or where to \nsubmit the form"
    },
    {
        "Attribute": "title",
        "Belongs to": "Global Attributes",
        "Description": "Specifies extra information about an element"
    },
    {
        "Attribute": "translate",
        "Belongs to": "Global Attributes",
        "Description": "Specifies whether the content of an element should be translated or not"
    },
    {
        "Attribute": "type",
        "Belongs to": "<a>, <button>, <embed>, <input>, <link>, <menu>, <object>, <script>, \n<source>, <style>",
        "Description": "Specifies the type of element"
    },
    {
        "Attribute": "usemap",
        "Belongs to": "<img>, <object>",
        "Description": "Specifies an image as a client-side image map"
    },
    {
        "Attribute": "value",
        "Belongs to": "<button>, <input>, <li>, <option>, \n<meter>, <progress>, <param>",
        "Description": "Specifies the value of the element"
    },
    {
        "Attribute": "width",
        "Belongs to": "<canvas>, <embed>, <iframe>, <img>, <input>, <object>, <video>",
        "Description": "Specifies the width of the element"
    },
    {
        "Attribute": "wrap",
        "Belongs to": "<textarea>",
        "Description": "Specifies how the text in a text area is to be wrapped when submitted in a \nform"
    }
]

app =   Flask(__name__)
# CORS(app)


@app.route('/', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        return jsonify(jsonData)

@app.route('/test/', methods = ['GET'])
def ReturnJSON2():
    if(request.method == 'GET'):
        return jsonify(jsonData2)

if __name__=='__main__':
   app.run(debug=True)