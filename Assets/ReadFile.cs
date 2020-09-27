using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;
using System.IO;

public class ReadFile : MonoBehaviour
{

    public Text textField;

    public void Read()
    {
        //Path del archivo
        string path = Application.dataPath + "MyTest.txt";

        //Si no existe el archivo
        if (!File.Exists(path))
        {
                //Error.
                Debug.Log("El archivo no existe.");
        }
        //SI el archivo si existe, lo lee
        else{
            using (StreamReader sr = File.OpenText(path))
            {
                string s;
                string text = "";
                while ((s = sr.ReadLine()) != null)
                {
                    //Debug.Log("yay");
                    //Console.WriteLine(s);
                    text += s;
                }

                textField.text = text;
            }
        }

    }
}
