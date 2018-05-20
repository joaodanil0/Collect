package projects.Collect.nodes.nodeImplementations;

import sinalgo.configuration.Configuration;
import sinalgo.configuration.CorruptConfigurationEntryException;
import sinalgo.configuration.WrongConfigurationException;
import sinalgo.gui.transformation.PositionTransformation;
import sinalgo.nodes.Node;
import sinalgo.nodes.messages.Inbox;
import sinalgo.nodes.messages.Message;
import sinalgo.runtime.Global;
import sinalgo.runtime.Main;
import sinalgo.tools.logging.Logging;

import java.awt.Color;
import java.awt.Graphics;
import java.util.ArrayList;

import projects.Collect.CustomGlobal;
import projects.Collect.nodes.messages.DataMessage;
import projects.Collect.nodes.timers.FloodingTimer;

public class Sink extends Node{

	
	/**
	 * Save the id messages received
	 */
	public ArrayList<Double>idMessages = new ArrayList<>();
	
	/**
	 * Compute the quantity of packets was send from all nodes
	 */
	static public double pcktsSentByNetwork = 0; 
	
	/**
	 * Compute the quantity of packets the sink received from network
	 */
	static public double pcktsReceivedFromNetwork = 0;
	
	/**
	 * Manage the log of simulation
	 */
	public Logging log;
	
	/**
	 * Give a name of simulation (Density, range e etc.)
	 */
	public String simulationType;
	
	/**
	 * The number of simulation (ex: numberOfNodes = 529 and simulation = 2, the namedir = 5292) 
	 */
	public int nameDir;
	
	/**
	 * Compute a quantity of packets received in each hour (initialize with number of hours)
	 */
	public double[] pcktsReceivedhour = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
									     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
									     0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
									     0,0,0,0,0,0,0,0,0,0,0,0
										};
	
	/**
	 * Compute a quantity of packets sent by network each hour (initialize with number of hours)
	 */
	public static double[] pcktsSenthour = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
										    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
										    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
										    0,0,0,0,0,0,0,0,0,0,0,0
										   };
	
	@Override
	public void handleMessages(Inbox inbox) {
		
		while(inbox.hasNext()) {
			
			Message msg = inbox.next();	
			
			if(msg instanceof DataMessage) {				
				processDataMessage((DataMessage) msg);
			}
		}
	}	
	
	@Override
	public void preStep() {
		
	}
	
	/**
	 * Send a flooding packet to network with the Sink position
	 */
	@Override	
	public void init() {
				
		setSinkPosition();		
		getParamLog();
		FloodingTimer t = new FloodingTimer(ID, getPosition(), ID, 0, null);
		t.startRelative(1, Sink.this);
		
	}

	@Override
	public void neighborhoodChange() {
		
	}

	@Override
	public void postStep() {
				
		if(Global.currentTime == Main.runtime.getNumberOfRounds()){
						
			
			double percentPcktArrived = (pcktsReceivedFromNetwork/pcktsSentByNetwork)*100;
					
					 	
			log = Logging.getLogger(simulationType + "_SimulacaoTX_" + nameDir + "/TXentrega.csv");
			log.logln("Porcentagem de pacotes recebidos,pacotes recebidos,pacotes enviados");
			log.logln(Double.toString(percentPcktArrived) + "," + pcktsReceivedFromNetwork + "," + pcktsSentByNetwork);
			
			log = Logging.getLogger(simulationType + "_Simulacao_" + nameDir + "/EntregasPorHora.csv");
			log.logln("Hora,Pacotes recebidos por hora, Pacotes enviados por hora, porcentagem de pacotes entregues");					
			for(int i = 0; i < (int)(Main.runtime.getNumberOfRounds()/3600); i++) {
				double percentDeliveredHours = (pcktsReceivedhour[i]/pcktsSenthour[i])*100;
				log.logln(i +"," + pcktsReceivedhour[i] + "," + pcktsSenthour[i] + "," + Double.toString(percentDeliveredHours));				
			}				
		}		
	}

	@Override
	public void checkRequirements() throws WrongConfigurationException {
		
	}
	
	public void draw(Graphics g, PositionTransformation pt, boolean highlight){
		
		drawNodeAsSquareWithText(g, pt, highlight, "", 2, Color.WHITE);
		setColor(Color.RED);		
	}

	//----------------------------------------------------------------------------
	//
	//					Custom methods			
	//
	//----------------------------------------------------------------------------
	
	/**
	 * Set the sink position in the mid of grid
	 */
	private void setSinkPosition() {
		setPosition(Configuration.dimX/2,Configuration.dimY/2,0);
	}
	
	/**
	 * Check if the idMessage is save  in the list
	 * @param idMessage Message to be checked
	 * @return True if packet received, False if not received
	 */
	public boolean isPcktReceived(double idMessage) {
		
		for(int i = 0; i< idMessages.size(); i++){			
			
			if(idMessages.get(i) == idMessage ){
				
				return true;
			}
		}
		return false;	
	}
	
	private void processDataMessage(DataMessage msg) {
		
		
		if(!isPcktReceived(msg.idMessage)){
			
			idMessages.add(msg.idMessage);
			pcktsReceivedFromNetwork++;	
			pcktsReceivedhour[msg.sendHour]++;
		}		
	}
	
	public void getParamLog() {
		try {
			
			nameDir = Configuration.getIntegerParameter("nameDir/name");
			
		} 
		catch (CorruptConfigurationEntryException e) {
			
			e.printStackTrace();
		}
		
		try {
			
			simulationType = Configuration.getStringParameter("simulationType/type");
			
		} 
		catch (CorruptConfigurationEntryException e) {
			
			e.printStackTrace();
		}
	}
	
	public static String showTime() {
		
		String aux;
			
		aux = "";
		
		if(CustomGlobal.hora < 10){
			
			aux += "0" + CustomGlobal.hora;
		}
		else{
			
			aux += CustomGlobal.hora;
		}
		
		if(CustomGlobal.minuto < 10){
			
			aux += ":0" + CustomGlobal.minuto;
		}
		else{
			
			aux += ":" + CustomGlobal.minuto;
		}
		
		if(CustomGlobal.segundo < 10){
			
			aux += ":0" + CustomGlobal.segundo;
			
		}
		else{
			
			aux += ":" +CustomGlobal.segundo;
		}
		
		return aux;
	}

	
}
