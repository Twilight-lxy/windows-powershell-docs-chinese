---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/enable-vmresourcemetering?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-VMResourceMetering
---

# 启用虚拟机资源计量功能

## 摘要
开始收集虚拟机或资源池的资源使用情况数据。

## 语法

### VMName（默认值）
```
Enable-VMResourceMetering [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-VMName] <String[]> [<CommonParameters>]
```

### ResourcePool
```
Enable-VMResourceMetering [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-ResourcePoolName] <String> [[-ResourcePoolType] <VMResourcePoolType>]
 [<CommonParameters>]
```

### VMObject
```
Enable-VMResourceMetering [-VM] <VirtualMachine[]> [<CommonParameters>]
```

## 描述
`Enable-VMResourceMetering` cmdlet 用于开始收集虚拟机或资源池的资源使用情况数据。

你可以使用 `Measure-VM` 或 `Measure-VMResourcePool` cmdlet 来获取这些数据。

如果启用了资源计量功能，但未配置任何 **NetworkAdapterAcls**，则 Hyper-V 会自动配置这些规则以测量总网络流量。如果要通过某个 IP 范围来测量网络流量，请在调用此 cmdlet 之前先为该 IP 范围配置相应的 **NetworkAdapterAcls**。（有关更多信息，请参阅 Add-VMNetworkAdapterAcl。）

## 示例

### 示例 1
```
PS C:\> Enable-VMResourceMetering -VMName TestVM
```

这个示例开始收集名为 TestVM 的虚拟机上的资源利用数据。

### 示例 2
```
PS C:\> Get-VM TestVM | Enable-VMResourceMetering
PS C:\> Get-VM TestVM | Format-List Name,ResourceMeteringEnabled
```

这个示例开始收集名为 TestResourcePool 的资源池的资源使用数据。（您可以通过查询其 ResourceMeteringEnabled 属性来确定该资源池是否启用了资源计量功能。）

### 示例 3
```
PS C:\> Enable-VMResourceMetering -ResourcePoolName TestResourcePool -ResourcePoolType Memory
PS C:\> Get-VMResourcePool -Name TestResourcePool -ResourcePoolType Memory | Format-List Name,ResourceMeteringEnabled
```

这个示例使用了两个命令：第一个命令用于启用资源计量功能，然后开始收集名为“TestResourcePool”的内存资源池的资源使用情况数据；（你可以通过查询该资源池的“ResourceMeteringEnabled”属性来判断其是否启用了资源计量功能。）第二个命令则用于检索这些数据，并将其格式化为列表形式。

### 示例 4
```
PS C:\> Enable-VMResourceMetering -Name TestResourcePool -ResourcePoolType @("Processor","VHD","Ethernet","Memory")
```

这个示例开始收集名为“TestResourcePool”的多个资源池的资源利用数据。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

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
指定要启用资源利用数据收集的虚拟机主机。允许使用 NetBIOS 名称、IP 地址和完全限定域名作为主机标识。默认值是本地计算机。可以使用 `localhost` 或一个点（.`）来明确表示本地计算机。

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
指定您希望收集资源利用率数据的资源池的友好名称。

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
指定您希望收集资源使用数据的资源池的资源类型。

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
指定您希望收集资源使用数据的虚拟机。

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
指定您想要收集资源使用数据的虚拟机的友好名称。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.HyperV.PowerShellvirtualMachine[]

### Microsoft.HyperV.PowerShell.VMResourcePoolType

## 输出

### 无

## 备注

## 相关链接

[Measure-VM](./Measure-VM.md)

[Measure-VMResourcePool](./Measure-VMResourcePool.md)

[禁用虚拟机资源计量功能](./ Disable-VMResourceMetering.md)

