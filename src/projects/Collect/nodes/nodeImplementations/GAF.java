package projects.Collect.nodes.nodeImplementations;

import java.awt.Color;
import java.awt.Graphics;
import java.util.ArrayList;

import projects.Collect.CustomGlobal;
import projects.Collect.models.energyModels.Energy;
import projects.Collect.nodes.messages.DataMessage;
import projects.Collect.nodes.messages.DiscoveryMessage;
import projects.Collect.nodes.messages.RoutingMessage;
import projects.Collect.nodes.timers.FloodingTimer;
import projects.Collect.nodes.timers.TaTimer;
import projects.Collect.nodes.timers.TdTimer;
import projects.Collect.nodes.timers.TsTimer;
import projects.Collect.nodes.nodeImplementations.GAF;
import projects.Collect.nodes.timers.SendTimer;
import sinalgo.configuration.Configuration;
import sinalgo.configuration.CorruptConfigurationEntryException;
import sinalgo.configuration.WrongConfigurationException;
import sinalgo.gui.transformation.PositionTransformation;
import sinalgo.nodes.Node;
import sinalgo.nodes.Position;
import sinalgo.nodes.messages.Inbox;
import sinalgo.nodes.messages.Message;
import sinalgo.runtime.Global;
import sinalgo.tools.logging.Logging;


public class GAF extends Node{
	
	/**
	 * This checks if sink's packet was received
	 */
	private boolean isConfigured = false;
	
	/**
	 * Sink position on the grid
	 */
	public Position sinkPosition;
	
	/**
	 * Sink identification
	 */
	public int sinkId;
	
	/**
	 * Distance from this node to the sink
	 */
	public double sinkDistance;
	
	/**
	 * The identification of the grid where this node stay
	 */
	public int gridID;
	
	/**
	 * The current state of the node
	 */
	public States state = States.discovery;
	
	/**
	 * Represent the battery of node
	 */
	public Energy battery;
	
	/**
	 * Check if sendTimer is active
	 */
	public boolean startSendTimer = false;
	
	/**
	 * Timer of send packet
	 */
	public SendTimer sendTimer;
			
	/**
	 * Check if TdTimer is active
	 */
	public boolean startTdTimer = false;
	
	/**
	 * Timer of discovery mode
	 */
	public TdTimer tdTimer;
		
	/**
	 * Check of TaTimer is active
	 */
	public boolean startTaTimer = false;
	
	/**
	 * Timer of active mode 
	 */
	public TaTimer taTimer;
	
	/**
	 * How long the node stay in active mode
	 */
	public double ta;
	
	/**
	 * Check of TsTimer is active
	 */
	public boolean startTsTimer = false;
	
	/**
	 * Timer of sleep mode 
	 */
	public TsTimer tsTimer;
	
	/**
	 * How long the node stay in sleep mode
	 */
	public double ts;
		
	/**
	 * Estimation node active time
	 */
	public double enat;
	
	/**
	 * How long the node stay in discovery mode
	 */
	public double td;
	
	/**
	 * Computes a quantity of data packets that have been sent
	 */
	public int dataPctSent = 0;
	
	/**
	 * Computes a quantity of Discovery packets that have been sent
	 */
	public int confPctSent = 0;
	
	/**
	 * Computes a quantity of data packets that gave been sent by hours
	 */
	public static int dataPctsSentByHour = 0;
	
	/**
	 * Computes a quantity of Discovery packets that gave been sent by hours
	 */
	public static int confPctsSentByHour = 0;
	
	/**
	 * Save the id messages received
	 */
	public ArrayList<Integer>idMessages = new ArrayList<>();
	
	/**
	 * Save the node ID from same virtual grid
	 */
	public ArrayList<Integer>neighbors = new ArrayList<>();
	
	/**
	 * Save energy whenever the node send Discovery Message
	 */
	public double energyTd = 0;
	
	/**
	 * Maximum energy of battery
	 */
	public double maxBatteryEnergy;
	
	/**
	 * Minimum energy of battery
	 */
	public double minBatteryEnergy;
	
	/**
	 * Minimum time between send the packets
	 */
	public double minTimeBetweenSends;
	
	/**
	 * Maximum time between send the packets
	 */
	public double maxTimeBetweenSends;
	
	/**
	 * Minimum solar intensity (for control packet sent)
	 */
	public double minSolarIntensity;
	
	/**
	 * Maximum solar intensity (for control packet sent)
	 */
	public double maxSolarIntensity;
	
	/**
	 * Manage the log of simulation
	 */
	Logging log;
	
	/**
	 * Give a name of simulation (Density, range e etc.)
	 */
	public String simulationType;
	
	/**
	 * The number of simulation (ex: numberOfNodes = 529 and simulation = 2, the namedir = 5292) 
	 */
	public int nameDir;
	
	/**
	 * Compute the quantity of dead nodes at the network
	 */
	public static int deadNode = 0;
	
	@Override
	public void handleMessages(Inbox inbox) {
	
		while(inbox.hasNext()) {
			
			Message msg = inbox.next();	
			
			if(msg instanceof RoutingMessage){
				
				if(hasEnergy() && (this.state != States.sleep)) {
					processRoutingMessage((RoutingMessage) msg);
					battery.gastaEnergiaRecebimento();
				}								
			}
			else if(msg instanceof DiscoveryMessage) {
				
				if(hasEnergy() && (this.state != States.sleep)) {
					battery.gastaEnergiaRecebimento();
					processDiscoveryMessage((DiscoveryMessage) msg);
					
				}
			}
			else if(msg instanceof DataMessage) {
				
				if(hasEnergy() && (this.state == States.active)) {
					processDataMessage((DataMessage) msg);
					battery.gastaEnergiaRecebimento();
				}
			}
		}
	}

	@Override
	public void preStep() {
		
		ta = calculateTimeSend();
	}

	@Override
	public void init() {
		
		divideGrid();
		getEnergyOfBatery();
		battery = new Energy(maxBatteryEnergy);
		getTimeSend();	
		getSolarIntensity();
		getParamLog();
	}

	@Override
	public void neighborhoodChange() {
		
		
	}
	
	boolean flag = false;
	@Override	
	public void postStep() {
				
		//mostraInfo(1);
		rechargeNode();
						
		if(isConfigured && hasEnergy() && (Global.currentTime >= 100) && !flag) {
			
			switch(state){
				
				case discovery:
					setColor(Color.YELLOW);
					discoveryMode();
					battery.gastaEnergiaIdle();
					break;
				case active:
					activeMode();
					setColor(Color.GREEN);	
					battery.gastaEnergiaIdle();
					break;
				case sleep:
					sleepMode();
					setColor(Color.RED);
					battery.modoSleep();
					break;							
			}			
		}
		else if(!isConfigured && hasEnergy()) {
			battery.gastaEnergiaIdle();
		}	
		else if(!hasEnergy()) {
			setColor(Color.MAGENTA);
			this.state = States.discovery;
			this.startTaTimer = false;
			this.startTdTimer = false;
			this.startTsTimer = false;
			flag = true;
		}

		if(hasEnergyPowerUp() && flag) {
			flag = false;
		}
		
		generateLog();
	}

	@Override
	public void checkRequirements() throws WrongConfigurationException {
		
		
	}
	
	//----------------------------------------------------------------------------
	//
	//					GAF methods			
	//
	//----------------------------------------------------------------------------
		
	/**
	 * Draw nodes with the grid identification
	 */
	public void draw(Graphics g, PositionTransformation pt, boolean highlight){
		drawNodeAsDiskWithText(g, pt, highlight, Integer.toString(gridID), 1, Color.BLACK);	
	}
	
	/**
	 * Called every time that routing message came in the node
	 * @param msg Data of routing message
	 */
	private void processRoutingMessage(RoutingMessage msg) {
					
		
		if(gridID == msg.gridID) {
			neighbors.add(msg.nodeID);
		}
				
		if(!isConfigured) {
			isConfigured = true;
			this.sinkPosition = msg.sinkPosition;
			this.sinkId = msg.sinkId;
			this.sinkDistance = getPosition().distanceTo(this.sinkPosition);
			FloodingTimer timer = new FloodingTimer(msg.sinkId, msg.sinkPosition, ID, gridID, this);
			timer.startRelative(1, GAF.this);				
		}
	}
	
	/**
	 * called every time that discovery message came in the node
	 * @param msg
	 */
	private void processDiscoveryMessage(DiscoveryMessage msg) {
		
		/*System.out.println("---------------------------");
		System.out.println("Node: " + msg.nodeID + " | gridID: " + msg.gridID + " | enat: " + msg.enat + " | state: " + msg.state + " | energyRemaining: " + msg.energyRemaining);
		System.out.println("Node: " +         ID + " | gridID: " +     gridID + " | enat: " +     enat + " | state: " +     state + " | energyRemaining: " + energyTd);
		System.out.println("Time arrived: " + Global.currentTime);
		System.out.println("---------------------------\n");
		*/
		
		if((this.state == States.discovery) && (msg.state == States.active) && (this.gridID == msg.gridID)) {
			this.state = States.sleep;
			this.ts = msg.enat;
		}
		else if((this.state == msg.state) && (this.gridID == msg.gridID)) {
			
			if(energyTd < msg.energyRemaining) {
				this.state = States.sleep;
				this.ts = msg.enat;
			}
		}
		else if(this.gridID != msg.gridID){
			// Do nothing
		}
		else if(this.state == States.sleep){
			// Do nothing			
		}
		else if(this.state == States.active){
			//Do nothing
		}
	}
	
	/**
	 * called every time that data message came in the node
	 * @param msg
	 */
	public void processDataMessage(DataMessage msg) {
		
		if((sinkDistance < msg.distanceSink) && !isPcktReceived(msg.idMessage) && hasEnergy()) {
			
			DataMessage msgReply = new DataMessage(msg.ID, sinkDistance, msg.idMessage, msg.gridMessage);
			idMessages.add(msg.idMessage);
			if(hasEnergy()) {
				dataPctSent++;	
				dataPctsSentByHour++;
				broadcast(msgReply);
				battery.gastaEnergiaEnvio();
			}
			
		}
	}
	
	/**
	 * Check if the idMessage is save  in the list
	 * @param idMessage Message to be checked
	 * @return True if packet received, False if not received
	 */
	public boolean isPcktReceived(int idMessage) {
		
		for(int i = 0; i< idMessages.size(); i++){			
			
			if(idMessages.get(i) == idMessage ){
				
				return true;
			}
		}
		return false;	
	}
	
	/**
	 * Divide nodes in virtual grids (based on GAF)
	 */
	private void divideGrid() {
		
		try {
			int range = Configuration.getIntegerParameter("UDG/rMax");
			double r = range/Math.sqrt(5);
			
			int num_cell = (int) (Configuration.dimX / r);
			
			for(int i = 0; i<= num_cell; i++){

				if(getPosition().xCoord >= i*r && getPosition().xCoord < (i+1)*r){
							
					for(int j = 0; j <= num_cell; j++){
					
						if(getPosition().yCoord >= j*r && getPosition().yCoord < (j+1)*r){
							
							gridID = Integer.parseInt(i + "" + j);	
							
						}	
					}		
				}	
			}	
		} 
		catch (CorruptConfigurationEntryException e) {
			e.printStackTrace();
		}		
	}
	
	/**
	 * The states of the nodes (based in GAF)
	 * @author joao
	 *
	 */
	public static enum States{
		sleep, discovery, active
	}
	
	/**
	 * Get the max energy of battery (from XML file)
	 */
	public void getEnergyOfBatery() {
		try {
			
			maxBatteryEnergy = Configuration.getDoubleParameter("maxEnergyOfBattery/energy");			
		} 
		catch (CorruptConfigurationEntryException e) {
			
			e.printStackTrace();
		}
		
		try {
			
			minBatteryEnergy = Configuration.getDoubleParameter("minEnergyOfBattery/energy");			
		} 
		catch (CorruptConfigurationEntryException e) {
			
			e.printStackTrace();
		}
	}
	
	/**
	 * Check if the node has energy to send a packet
	 * @return true if has energy. False if don't have energy
	 */
	public boolean hasEnergy() {
		if(battery.getEnergiaAtual() >= battery.getEnergiaEnvio()) 
			return true;
				
		return false;
	}
	
	/**
	 * Check if the node has energy to power up after full drain battery in harvesting
	 * @return true if has energy. False if don't have energy
	 */
	public boolean hasEnergyPowerUp() {
		if(battery.getEnergiaAtual() >= battery.getEnergiaEnvio()*100) 
			return true;
				
		return false;
	}
	
	/**
	 * Make process of discovery mode (based in GAF)
	 */
	public void discoveryMode() {
		
		if(!startTdTimer) {
			
			/**
			 * How long the node stay in discovery mode
			 */
			
			
			td = 10;			
			enat = ta;
			
			battery.gastaEnergiaEnvio();			
			if(hasEnergy()) {
				DiscoveryMessage msg = new DiscoveryMessage(ID, gridID, enat, state, battery.getEnergiaAtual());			
				broadcast(msg);
				confPctSent++;
				confPctsSentByHour++;
				energyTd = battery.getEnergiaAtual();
				
				tdTimer = new TdTimer(ID, gridID, enat, state, this, battery.getEnergiaAtual());
				tdTimer.startRelative(td, GAF.this);
				startTdTimer = true;
			}			
		}			
	}
	
	/**
	 * Make process of active mode (based in GAF)
	 */
	public void activeMode() {
		
		if(!startTaTimer) {
			
			taTimer = new TaTimer(this);
			taTimer.startRelative(ta, GAF.this);
			startTaTimer = true;
			td = (ta/6);
		}
		
		if(!startSendTimer) {
			sendTimer = new SendTimer(this);
			sendTimer.startRelative(ta/2, GAF.this);
			startSendTimer = true;
		}
		
		enat = enat - 1;
		
		if(!startTdTimer && (enat > td)) {			
			
			tdTimer = new TdTimer(ID, gridID, enat, state, this, battery.getEnergiaAtual());
			tdTimer.startRelative(td, GAF.this);
			startTdTimer = true;
		}	
	}

	/**
	 * Make process of sleep mode (based in GAF)
	 */
	public void sleepMode() {
		
		if(!startTsTimer) {
			tsTimer = new TsTimer(this);
			tsTimer.startRelative(ts, GAF.this);
			startTsTimer = true;
		}		
	}
	
	//-------------------------------------------------------------
	//
	//			Harvesting methods
	//
	//-------------------------------------------------------------
	
	/**
	 * Recharge the battery of the node
	 */
	public void rechargeNode() {
		
		if(CustomGlobal.dia && (battery.getEnergiaAtual() < battery.getEnergiaMaxima())){
			battery.recarrega();
		}
	}
	
	//-------------------------------------------------------------
	//
	//			Control Harvesting
	//
	//-------------------------------------------------------------
	
	/**
	 * Get the times of send from XML
	 */
	public void getTimeSend() {
		try {
			minTimeBetweenSends = Configuration.getDoubleParameter("minTimeBetweenSends/time");
		} 
		catch (CorruptConfigurationEntryException e) {
			
			e.printStackTrace();
		}
		
		try {
			maxTimeBetweenSends = Configuration.getDoubleParameter("maxTimeBetweenSends/time");
		} 
		catch (CorruptConfigurationEntryException e) {
			
			e.printStackTrace();
		}
	}
	
	/**
	 * Get the solar intensity from XML
	 */
	public void getSolarIntensity() {
		try {
			minSolarIntensity = Configuration.getDoubleParameter("minSolarIntensity/intensity");
		} 
		catch (CorruptConfigurationEntryException e) {
			
			e.printStackTrace();
		}
		
		try {
			maxSolarIntensity = Configuration.getDoubleParameter("maxSolarIntensity/intensity");
		} 
		catch (CorruptConfigurationEntryException e) {
			
			e.printStackTrace();
		}
	}
	
	/**
	 * Calculate the time that node send a package
	 */
	public double calculateTimeSend() {
		
		double solarIntensity;
		
		if(CustomGlobal.intensidadeSolar < 0)
			solarIntensity = 0;
		else
			solarIntensity = CustomGlobal.intensidadeSolar;
		
		double controlEnergy = (((battery.getEnergiaAtual()) - maxBatteryEnergy)/(minBatteryEnergy - maxBatteryEnergy));
		double controlSolarInt = (((2*solarIntensity) - maxSolarIntensity)/(minSolarIntensity - maxSolarIntensity));
		double time = ((maxTimeBetweenSends - minTimeBetweenSends)*(controlEnergy + controlSolarInt) + 2*minTimeBetweenSends)/2;
		
		
		if(time <= minTimeBetweenSends)
			time = minTimeBetweenSends;
		
		//System.out.println("Time: " + Global.currentTime/3600 + " | time: " + time + " | Si: " + solarIntensity);
		
		return time;
	}
	
		
	//-------------------------------------------------------------
	//
	//			Debug
	//
	//--------------------------------------------------------------
	
	/**
	 * Mostra informações detalhadas de um determinado nó (no modo terminal)
	 * @param id define qual nó deve ser avaliado
	 */
	
	double deleteme = 0;
	public void mostraInfo(int id){
		
		if(ID == id){
			
			System.out.printf("D: %d", CustomGlobal.num_dias);
			
			System.out.printf(" | Hora: ");
			
			if(CustomGlobal.hora < 10){
				
				System.out.printf("0%d:", CustomGlobal.hora);
			}
			else{
				
				System.out.printf("%d:", CustomGlobal.hora);
			}
			
			if(CustomGlobal.minuto < 10){
				
				System.out.printf("0%d:", CustomGlobal.minuto);
			}
			else{
				
				System.out.printf("%d:", CustomGlobal.minuto);
			}
			
			if(CustomGlobal.segundo < 10){
				
				System.out.printf("0%d", CustomGlobal.segundo);
				
			}
			else{
				
				System.out.printf("%d", CustomGlobal.segundo);
			}
						
			System.out.printf("| Energia: %.5f | ", battery.getEnergiaAtual());
			System.out.print("Dia: " + Boolean.valueOf(CustomGlobal.dia));
			System.out.print(" | Carregando: " + Boolean.valueOf(CustomGlobal.dia));
			
			if(CustomGlobal.dia){
				deleteme += battery.getEnergiaPainel();
				System.out.printf(" (%f) | (%f) ",  battery.getEnergiaPainel(), deleteme);
				
			}
			else{
				
				System.out.print(" (0.0) ");
				deleteme = 0;
			}
			
			System.out.println("| Tempo: " + ta);
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
	
public void generateLog(){
		
		if(Global.currentTime == 1){
			log = Logging.getLogger(simulationType +"_Simulacao_" + nameDir + "/Energia.csv");
			if(ID == 1) {
				log.logln("Tempo decorrido,Energia do no,Coordenada X,Coordenada Y,Pacotes Enviados,Pacotes de confi"
						+ "guracao,Enviados+Configuracao");
			}
			
			 
			 log.logln(Double.toString(Global.currentTime/3600) + "," + Double.toString(battery.getEnergiaAtual())+ ","
					 + Double.toString(getPosition().xCoord) + "," +  Double.toString(getPosition().yCoord) + ","
					 + dataPctSent + "," + confPctSent + "," + (dataPctSent + confPctSent));
			 
			 
			 
			 
			 if(ID == 1) {
				 log = Logging.getLogger(simulationType +"_Simulacao_" + nameDir + "/PctsHora.csv");	
				 log.logln("Hora,Pacotes enviados por hora,Pacotes configuracao por hora,enviados+configuracao");
				 log.logln(Global.currentTime/3600 +"," + dataPctsSentByHour + "," + confPctsSentByHour + "," + (dataPctsSentByHour + confPctsSentByHour));
				 
				 dataPctsSentByHour = 0;
				 confPctsSentByHour = 0;
			 }
			 			 
			 
			 
			 if(!hasEnergy()) {
				deadNode++;
			 }
				
			
			
			if(ID == 1) {
				log = Logging.getLogger(simulationType +"_Simulacao_" + nameDir + "/NosMortos.csv");
				log.logln("Hora,Quantidade de nos mortos");
				log.logln(Global.currentTime/3600 +"," + deadNode);
				deadNode = 0;
			}
			
				
			
			 
			 
			 
		}
		
		if(Global.currentTime % 3600 == 0) {
			
			
			if(ID == 1) {
				log = Logging.getLogger(simulationType +"_Simulacao_" + nameDir + "/PctsHora.csv");
				log.logln(Global.currentTime/3600 +"," + dataPctsSentByHour + "," + confPctsSentByHour + "," + (dataPctsSentByHour + confPctsSentByHour));
				 
				dataPctsSentByHour = 0;
				confPctsSentByHour = 0;
			}			
			
			
			if(!hasEnergy()) {
				deadNode++;
			}
			
			if(ID == 1) {	
				log = Logging.getLogger(simulationType +"_Simulacao_" + nameDir + "/NosMortos.csv");
				log.logln(Global.currentTime/3600 +"," + deadNode);
				deadNode = 0;
			}
			
		}
		
		if(Global.currentTime % 60 == 0){
			log = Logging.getLogger(simulationType +"_Simulacao_" + nameDir + "/Energia.csv");
			
			log.logln(Double.toString(Global.currentTime/3600) + "," + Double.toString(battery.getEnergiaAtual()) + ","
				  + Double.toString(getPosition().xCoord) + "," +  Double.toString(getPosition().yCoord) + "," 
				  + dataPctSent + "," + confPctSent + "," + (dataPctSent + confPctSent));
			
		}			
	}


}
