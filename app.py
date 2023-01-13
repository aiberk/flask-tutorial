from flask import Flask,jsonify,request
path="Python/tutorial/htmlTags.json"


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
  
app =   Flask(__name__)
  
@app.route('/', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        return jsonify(jsonData)
  
if __name__=='__main__':
    app.run(debug=True)