package projects.Collect.nodes.timers;

import projects.Collect.nodes.nodeImplementations.GAF;
import projects.Collect.nodes.nodeImplementations.GAF.States;
import sinalgo.nodes.timers.Timer;


public class TaTimer extends Timer {

	/**
	 * The instance of the node that call the timer
	 */
	public GAF gaf;
	
	public TaTimer(GAF gaf) {
		
		this.gaf = gaf;
	}

	@Override
	public void fire() {
				
		if(this.gaf.state == States.active) {
			
			this.gaf.state = States.discovery;
			this.gaf.startTaTimer = false;	
			this.gaf.startSendTimer = false;		
		}		
	}

}
