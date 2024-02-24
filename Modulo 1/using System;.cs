using System;
using System.ServiceProcess;

namespace MiServicio
{
    class Program : ServiceBase
    {
        static void Main(string[] args)
        {
            ServiceBase[] ServicesToRun;
            ServicesToRun = new ServiceBase[]
            {
                new Program()
            };
            ServiceBase.Run(ServicesToRun);
        }

        public Program()
        {
            this.ServiceName = "MiServicio";
        }

        protected override void OnStart(string[] args)
        {
            
        }

        protected override void OnStop()
        {
            
        }
    }
}
