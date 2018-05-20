package projects.Collect.nodes.timers;

import java.util.Random;

import projects.Collect.CustomGlobal;
import projects.Collect.nodes.messages.DataMessage;
import projects.Collect.nodes.nodeImplementations.GAF;
import projects.Collect.nodes.nodeImplementations.Sink;
import projects.Collect.nodes.nodeImplementations.GAF.States;
import sinalgo.nodes.timers.Timer;

public class SendTimer extends Timer {
	
	/**
	 * The instance of the node that call the timer
	 */
	public GAF gaf;
	public Random random = new Random();
	
	public SendTimer(GAF gaf) {
		
		this.gaf = gaf;
	}
	
	@Override
	public void fire() {
		
		if(this.gaf.state == States.active) {
			
			double idMessage = this.gaf.ID*100000  + (random.nextInt(999) + random.nextGaussian());
			
			if(this.gaf.hasEnergy()) {
				this.gaf.dataPctsSentByHour++;
				Sink.pcktsSentByNetwork++;
				this.gaf.dataPctSent++;								
				Sink.pcktsSenthour[CustomGlobal.hora + 24*CustomGlobal.num_dias]++;	
				DataMessage msg = new DataMessage(this.gaf.ID, this.gaf.sinkDistance, idMessage, this.gaf.gridID, CustomGlobal.hora + 24*CustomGlobal.num_dias);
				this.node.broadcast(msg);
				this.gaf.battery.gastaEnergiaEnvio();
			}			
		}
	}
}
