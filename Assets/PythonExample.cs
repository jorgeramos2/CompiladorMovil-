using System.Collections;
using System.Collections.Generic;
using IronPython.Hosting;
using UnityEngine;

//Este script realiza la conexión con python y ejecuta el script Greeter.
public class PythonExample : MonoBehaviour {

    // Use this for initialization
    void Start()
    {
        //Instrucciones para inizializar ironpython
        var engine = Python.CreateEngine();
        ICollection<string> searchPaths = engine.GetSearchPaths();

        //Path to the folder of greeter.py
        searchPaths.Add(Application.dataPath);
        //Path to the Python standard library
        searchPaths.Add(Application.dataPath + @"\Plugins\Lib\");
        engine.SetSearchPaths(searchPaths);

        dynamic py = engine.ExecuteFile(Application.dataPath + @"\greeter.py");
        dynamic greeter = py.Greeter("Mika");

        //Desplegar la ejecución del script
        Debug.Log(greeter.greet());
        Debug.Log(greeter.random_number(1,5));
    }

    //Repetir el código en otra función nadamas para probarlo dando click en un botón
    public void Display()
    {
        //Instrucciones para inizializar ironpython
        var engine = Python.CreateEngine();
        ICollection<string> searchPaths = engine.GetSearchPaths();

        //Path to the folder of greeter.py
        searchPaths.Add(Application.dataPath);
        //Path to the Python standard library
        searchPaths.Add(Application.dataPath + @"\Plugins\Lib\");
        engine.SetSearchPaths(searchPaths);

        dynamic py = engine.ExecuteFile(Application.dataPath + @"\greeter.py");
        dynamic greeter = py.Greeter("Mika");

        //Desplegar la ejecución del script
        Debug.Log(greeter.greet());
        Debug.Log(greeter.random_number(1,5));
    }
    

    // Update is called once per frame
    void Update () {
		
	}
}
