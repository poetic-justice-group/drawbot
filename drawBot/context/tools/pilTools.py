import AppKit
import io


def pilToNSImage(pilImage):
    buffer = io.BytesIO()
    pilImage.save(buffer, "PNG")
    data = buffer.getvalue()
    data = AppKit.NSData.dataWithBytes_length_(data, len(data))
    nsImage = AppKit.NSImage.alloc().initWithData_(data)
    return nsImage
