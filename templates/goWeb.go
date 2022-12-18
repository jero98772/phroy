//{name} - by {author}
package main
import ("fmt"
	"net/http"
	"text/template"
	)

func Index(rw http.ResponseWriter,r *http.Request){
	template, _ := template.ParseFiles("templates/index.html")
	template.Execute(rw,nil)
}
func main(){
	http.HandleFunc("/",Index)
	port :="9600"
	fmt.Println("run at localhost:"+port)
	http.ListenAndServe("localhost:"+port,nil)

}