---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/start-vminitialreplication?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Start-VMInitialReplication
---

# 启动虚拟机初始复制过程

## 摘要
开始复制虚拟机。

## 语法

### VMName（默认值）
```
Start-VMInitialReplication [-ComputerName <String[]>] [-VMName] <String[]> [-DestinationPath <String>]
 [-InitialReplicationStartTime <DateTime>] [-UseBackup] [-AsJob] [-Passthru] [-CimSession <CimSession[]>]
 [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Start-VMInitialReplication [-VM] <VirtualMachine[]> [-DestinationPath <String>]
 [-InitialReplicationStartTime <DateTime>] [-UseBackup] [-AsJob] [-Passthru] [-CimSession <CimSession[]>]
 [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 虚拟机复制（VMReplication）
```
Start-VMInitialReplication [-VMReplication] <VMReplication[]> [-DestinationPath <String>]
 [-InitialReplicationStartTime <DateTime>] [-UseBackup] [-AsJob] [-Passthru] [-CimSession <CimSession[]>]
 [-Credential <PSCredential[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Start-VMInitialReplication` cmdlet 使用您选择的方法来启动虚拟机的复制过程。此外，您还可以将复制任务安排在最多 7 天后开始执行。

## 示例

#### 示例 1
```
PS C:\> Start-VMInitialReplication VM01
```

这个示例开始通过网络对虚拟机VM01进行初始复制（即从源服务器复制到目标服务器）。

### 示例 2
```
PS C:\> Start-VMInitialReplication *
```

这个示例启动了对本地Hyper-V主机上所有尚未完成初始复制的虚拟机的网络复制过程。

### 示例 3
```
PS C:\> Start-VMInitialReplication * -DestinationPath R:\IRLoc
```

此示例将所有在本地 Hyper-V 主机上处于初始复制待处理状态的虚拟机的初始复制数据导出到路径 R:\IRLoc。该示例假设该路径是一个外部驱动器，这个驱动器会被发送到副本站点，以便完成初始复制过程。

### 示例 4
```
PS C:\> Enable-VMReplication VM01 -AsReplica -computername MyReplica.contoso.com
PS C:\> Enable-VMReplication VMO1 -ReplicaServerName ReplicaServer01 -ReplicaServerPort 80 -AuthenticationType Kerberos -computername MyPrimary.contoso.comPS
PS C:\> Start-VMInitialReplication VM01 -usebackup -computername MyPrimary.contoso.com
```

这个示例使用了几条连续的命令来从备份开始初始复制过程。首先，它将恢复后的虚拟机VM01在副本服务器上设置为副本虚拟机。接着，它启用VM01与主服务器之间的复制功能。最后，它启动初始复制过程，以副本服务器上的恢复后的VM01副本作为复制的基准。

### 示例 5
```
PS C:\> $VMRepl = Get-VMReplication -VMName MyVM
PS C:\> Start-VMInitialReplication -VMReplication $VMRepl
```

第一个命令返回一个名为“MyVM”的虚拟机的VMReplication对象，并将其存储在变量$VMRepl中。

第二个cmdlet随后使用这个对象来启动已存储虚拟机的初始复制过程。

## 参数

### -AsJob
将此 cmdlet 作为后台作业运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于启动虚拟机复制操作的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定的域名来进行选择。默认值为本地计算机。如果需要明确指定本地计算机，可以使用 `localhost` 或点号（.）。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
默认值；常规设置 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DestinationPath
指定在初始复制过程中用于复制文件的路径；假设使用外部介质作为初始复制的方法。外部介质通常是一个可移动驱动器，会被送到副本服务器的位置。当外部介质到达副本站点后，请在副本虚拟机上使用 **Import-InitialVMReplication** cmdlet 来复制文件。

```yaml
Type: String
Parameter Sets: (All)
Aliases: IRLoc

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -InitialReplicationStartTime
用于指定初始复制开始的时间，特别是在计划将初始复制延迟到以后执行的情况下。您可以选择的时间最多为7天后。如果未指定此参数，则初始复制会立即开始。

```yaml
Type: DateTime
Parameter Sets: (All)
Aliases: IRTime

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定要将一个虚拟机对象传递给代表该虚拟机的管道，以便在该虚拟机上启动复制操作。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UseBackup
这表示您希望使用该虚拟机的一个副本作为副本服务器上进行初始复制的基础。只有当在主虚拟机上启用复制功能时指定了此选项，才需要选择该选项。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定要启动复制的虚拟机。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
默认值；常规设置 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定要启动复制的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
默认值；常规设置 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMReplication
指定一个用于表示要启动的复制的对象。您可以通过 **Get-VMReplication** cmdlet 获取该对象。

```yaml
Type: VMReplication[]
Parameter Sets: VMReplication
Aliases:

Required: True
Position: 0
默认值；常规设置 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行会发生的结果。但实际上该cmdlet并未被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
默认值；常规设置 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值；常规设置

### Microsoft.HyperV POWERShell.VirtualMachine
如果指定了 `-PassThru`，

## 备注

## 相关链接

