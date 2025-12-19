---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/reset-vmresourcemetering?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Reset-VMResourceMetering
---

# 重置虚拟机资源计量数据

## 摘要
重置由 Hyper-V 资源计量工具收集的资源使用数据。

## 语法

### VMName（默认值）
```
Reset-VMResourceMetering [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [<CommonParameters>]
```

### ResourcePool
```
Reset-VMResourceMetering [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-ResourcePoolName] <String> [[-ResourcePoolType] <VMResourcePoolType>] [<CommonParameters>]
```

### VMObject
```
Reset-VMResourceMetering [-VM] <VirtualMachine[]> [<CommonParameters>]
```

## 描述
`Reset-VMResourceMetering` cmdlet 用于重置由 Hyper-V 资源计量系统收集的资源使用数据。

当调用此cmdlet时，截至当前时间点收集到的虚拟机或资源池的资源利用率数据将被删除。重置后，Hyper-V会继续收集资源利用率数据。

## 示例

### 示例 1
```
PS C:\> Reset-VMResourceMetering -VMName TestVM
```

在名为TestVM的虚拟机上重置资源利用数据收集功能。

### 示例 2
```
PS C:\> Reset-VMResourceMetering -ResourcePoolName TestResourcePool -ResourcePoolType Memory
```

重置名为 TestResourcePool 的单个资源池的资源利用数据收集功能。该资源池的类型为 Memory（内存）。

### 示例 3
```
PS C:\> Get-VMResourcePool -ResourcePoolType @("Processor","VHD","Ethernet","Memory") | Reset-VMResourceMetering
```

重置虚拟机主机上所有支持的资源池类型的资源利用率数据收集功能。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: VMName, ResourcePool
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个虚拟机主机，这些主机的资源利用率数据需要被重置。允许使用 NetBIOS 名称、IP 地址和完全限定域名作为主机标识。默认值是本地计算机。可以使用 `localhost` 或点号（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName, ResourcePool
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值是当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: VMName, ResourcePool
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResourcePoolName
指定要重置资源利用数据的虚拟机资源池的友好名称。

```yaml
Type: String
Parameter Sets: ResourcePool
Aliases: Name

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -ResourcePoolType
指定需要重置资源使用数据的虚拟机资源池的资源类型。

```yaml
Type: VMResourcePoolType
Parameter Sets: ResourcePool
Aliases:
Accepted values: Ethernet, Memory, Processor, VHD

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -VM
指定要重置资源利用数据的虚拟机。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定要重置资源使用数据的虚拟机的友好名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.HyperV.PowerShell.VirtualMachine[]

### Microsoft.HyperV.PowerShell.VMResourcePoolType

## 输出

### 无

## 备注

## 相关链接

[Measure-VM](./Measure-VM.md)

[Measure-VMResourcePool](./Measure-VMResourcePool.md)
