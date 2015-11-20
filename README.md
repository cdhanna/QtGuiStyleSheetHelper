# QtGuiStyleSheetHelper
A utility class for programmatically creating QtQui style sheets.
-----------------------------------------------------------------

### To Use

Download the python file, drop it in your project folder, and make sure to add the import statement in your main code.
```python
from QtStyleHelper import Styles
```

### Tutorial

PySide's QtGui code is great. It lets you style widgets using css-like style sheets. Look here for the [Style Sheet Reference page](http://doc.qt.io/qt-4.8/stylesheet.html)

But managing the style sheets is a bit of pain. You could make a big long string yourself, like 

```python
myStyle = 'QLabel{ background-color: red; }'
```

But that'd get annoying really fast if you had a lot of styling to do. This utility allows you to do stuff more like this

```python
s = Styles()
labels = (s['QLabel']
        .set('background-color', 'red')
    )
```

Its more code, yes, but it is way easier to extend later. For example, if you wanted to implement some of the given [examples](http://doc.qt.io/qt-4.8/stylesheet-examples.html), writing the string version would be a pain, but writing it with this utility class is a breeze. Take the pushbutton style example...

```css
QPushButton#evilButton {
    background-color: red;
    border-style: outset;
    border-width: 2px;
    border-color: beige;
}
```

To implement that in the utility, it looks like

```python
s = Styles()
evilButton = (s['QPushButton#evilButton']
        .set('background-color', 'red')
        .set('border-style', 'outset')
        .set('border-width', '2px')
        .set('border-color', 'beige')
    )
```

I'm not going to write out the string assembly version of that, because it'd be nasty to look at. Anyway, to apply the style, you just call the `setStyleSheet` function with `str(s)`. 

```python
evilWidget = QPushButton()
evilWidget.setObjectName('evilButton')

s = Styles()
# assign evilButton like in the example above...

evilWidget.setStyleSheet(str(s)) #important bit that sets the style.
```

Thats pretty much it. The rest is up to you! Quick notes about it

* to select an object, use `s['selection']` where _selection_ is any valid Qt Style Sheet selection. You can see those in the [documentation.](http://doc.qt.io/qt-4.8/stylesheet.html)
* You can chain `set` methods together like I did in the examples, but you can also call them one after another.
    
    ```python
    s = Styles()
    labels = s['QLabel']
    labels.set('background-color', 'red')
    labels.set('color', 'green')
    ```