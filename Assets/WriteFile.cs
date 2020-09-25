using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;
using System.IO;

//Este script sirve para obtener texto de un inputfield y escribirlo en un archivo. 
public class WriteFile : MonoBehaviour
{
    //Obtiene el inputfield donde se escribirá el código
    public InputField mainInputField;

    //Función para escribir el texto obtenido del inputfield en un archivo.
    public void Write()
    {

     
        String ObjectsText = mainInputField.text;


        //Path del archivo
        string path = Application.dataPath + "MyTest.txt";

        //Si no existe el archivo lo crea y escribe
        if (!File.Exists(path))
        {
            //Crear archivo.
            using (StreamWriter sw = File.CreateText(path))
            {
                //Escribir.
                sw.WriteLine(ObjectsText);
            }
        }

        //Si el archivo ya existe, lo borra, crea de nuevo, y escribe.
        else
        {
            //Borrar archivo anterior.
            File.Delete(path);
            //Crear archivo.
            using (StreamWriter sw = File.CreateText(path))
            {
                //Escribir.
                sw.WriteLine(ObjectsText);
            }
        }

        // Open the file to read from.
        /*
        using (StreamReader sr = File.OpenText(path))
        {
            string s;
            while ((s = sr.ReadLine()) != null)
            {
                Console.WriteLine(s);
            }
        }*/
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
