package edu.packt.neuralnet.Chapter1;

import java.util.ArrayList;

/**
 * 解释
 * <p>
 * 神经网络拓补结构在该类中是固定的：
 * 输入层：有2个神经元
 * 隐藏层：2层，每层3个神经元
 * 输出层：1个神经元
 */
public class NeuralNet {

    private InputLayer inputLayer;
    private HiddenLayer hiddenLayer;
    private ArrayList<HiddenLayer> listOfHiddenLayer;
    private OutputLayer outputLayer;
    private int numberOfHiddenLayers;

    public void initNet() {
        inputLayer = new InputLayer();
        inputLayer.setNumberOfNeuronsInLayer(2);

        numberOfHiddenLayers = 2;
        listOfHiddenLayer = new ArrayList<HiddenLayer>();
        for (int i = 0; i < numberOfHiddenLayers; i++) {
            hiddenLayer = new HiddenLayer();
            hiddenLayer.setNumberOfNeuronsInLayer(3);
            listOfHiddenLayer.add(hiddenLayer);
        }

        outputLayer = new OutputLayer();
        outputLayer.setNumberOfNeuronsInLayer(1);

        inputLayer = inputLayer.initLayer(inputLayer);

        listOfHiddenLayer = hiddenLayer.initLayer(hiddenLayer, listOfHiddenLayer, inputLayer, outputLayer);

        outputLayer = outputLayer.initLayer(outputLayer);

    }

    public void printNet() {
        inputLayer.printLayer(inputLayer);
        System.out.println();
        hiddenLayer.printLayer(listOfHiddenLayer);
        System.out.println();
        outputLayer.printLayer(outputLayer);
    }

}
