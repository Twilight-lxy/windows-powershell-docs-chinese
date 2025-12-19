---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/start-vmfailover?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Start-VMFailover
---

# 启动虚拟机故障转移

## 摘要
在虚拟机上启动故障转移（failover）过程。

## 语法

### VMName（默认值）
```
Start-VMFailover [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [-Prepare] [-AsJob] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMName_Test
```
Start-VMFailover [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [-AsTest] [-AsJob] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMObject
```
Start-VMFailover [-VM] <VirtualMachine[]> [-Prepare] [-AsJob] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### VMObject_Test
```
Start-VMFailover [-VM] <VirtualMachine[]> [-AsTest] [-AsJob] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### VMSnapshot
```
Start-VMFailover [-VMRecoverySnapshot] <VMSnapshot> [-AsJob] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### VMSnapshot_Test
```
Start-VMFailover [-VMRecoverySnapshot] <VMSnapshot> [-AsTest] [-AsJob] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
**Start-VMFailover** cmdlet 可用于以下任务：

- Fail over a Replica virtual machine to a chosen recovery point.
- Start a planned failover on a primary virtual machine.
- Create a test virtual machine on a Replica virtual machine.

## 示例

#### 示例 1
```
PS C:\> Get-VMSnapshot VM01 -Name Snapshot01 | Start-VMFailover
```

这个示例开始执行名为VM01的虚拟机的故障转移操作，并使用恢复点Snapshot01来进行恢复。

注意：恢复点是以快照的形式存储的。要获取所有快照的列表，请使用 **Get-VMSnapshot** cmdlet。

### 示例 2
```
PS C:\> Start-VMFailover VM01 -AsTest
```

这个示例启动了对名为VM01的虚拟机的测试故障转移（即当该虚拟机出现故障时，系统会自动切换到备用虚拟机）。

### 示例 3
```
PS C:\> Get-VMSnapshot VM01 -Name Snapshot01 | Start-VMFailover -AsTest
```

开始对名为VM01的虚拟机执行测试故障转移操作，并使用恢复点Snapshot01来进行处理。

### 示例 4
```
PS C:\> Start-VMFailover -Prepare -VMName VM01  -computername MyPrimary.contoso.com
PS C:\> Start-VMFailover -VMName VM01 -computername MyReplica.contoso.com
PS C:\> Set-VMReplication -Reverse -VMName VM01 -computername MyReplica.contoso.com
PS C:\> Start-VM -VMName VM01 -computername MyReplica.contoso.com
```

这个示例展示了用于执行计划中的故障转移（planned failover）的相关 cmdlet。第一个命令通过复制所有待处理的更改来为名为 VM01 的主虚拟机的故障转移做准备；第二个命令将备用虚拟机切换为主虚拟机；第三个命令则将备用虚拟机重新设置为主虚拟机；最后一个命令用于启动那些从备用状态被切换回主状态的虚拟机。

## 参数

### -AsJob
以后台作业的形式运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AsTest
使用所选的恢复点创建一个测试虚拟机。您可以使用该测试虚拟机来验证副本虚拟机的运行情况。要停止测试中的故障转移操作，请使用 **Stop-VMFailover** cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: VMName_Test, VMObject_Test, VMSnapshot_Test
Aliases:

Required: True
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: VMName, VMName_Test
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于启动故障转移的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行选择。默认值是本地计算机。可以使用 `localhost` 或点号（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName, VMName_Test
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您确认是否要执行该操作。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
默认值 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: VMName, VMName_Test
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定要将一个虚拟机对象传递给代表要启动故障转移操作的该虚拟机的管道（pipeline）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Prepare
在主虚拟机上启动计划中的故障转移操作，并复制所有待处理的更改。要完成计划中的故障转移，请使用 **Set-VMReplication** 和 **Start-VM** cmdlet，具体操作请参见示例 4。

注意：为了准备故障转移，必须关闭主虚拟机。

```yaml
Type: SwitchParameter
Parameter Sets: VMName, VMObject
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定要启动故障转移的虚拟机。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject, VMObject_Test
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定要启动故障转移的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName, VMName_Test
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMRecoverySnapshot
指定在故障转移过程中使用的恢复快照。（对于计划好的故障转移来说，此参数是可选的。）

```yaml
Type: VMSnapshot
Parameter Sets: VMSnapshot, VMSnapshot_Test
Aliases: VMRecoveryCheckpoint

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。不过实际上这个cmdlet并没有被执行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
默认值 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell.VirtualMachine
如果指定了 `-PassThru`。

## 备注

## 相关链接

