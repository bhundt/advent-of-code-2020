import Foundation

//place the file Textfile.txt in the executable directory
let file = "input"
if let path = Bundle.main.path(forResource: file, ofType: "txt"){
    do {
        let data = try String(contentsOfFile: path, encoding: .utf8)
        let myStrings = data.components(separatedBy: .newlines)
        let text = myStrings.joined(separator: "\n")
        print("\(text)")
    } catch {
        print(error)
    }
}
