---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmnetworkadapterfailoverconfiguration?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMNetworkAdapterFailoverConfiguration
---

# Get-VMNetworkAdapterFailoverConfiguration

## 摘要
获取用于虚拟机故障转移的虚拟网络适配器IP地址。

## 语法

### VMName（默认值）
```
Get-VMNetworkAdapterFailoverConfiguration [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-VMName] <String[]> [-VMNetworkAdapterName <String>] [<CommonParameters>]
```

### VMObject
```
Get-VMNetworkAdapterFailoverConfiguration [-VM] <VirtualMachine[]> [-VMNetworkAdapterName <String>]
 [<CommonParameters>]
```

### ResourceObject
```
Get-VMNetworkAdapterFailoverConfiguration [-VMNetworkAdapter] <VMNetworkAdapter[]> [<CommonParameters>]
```

## 描述
`Get-VMNetworkAdapterFailoverConfiguration` cmdlet 用于获取虚拟网络适配器的 IP 地址配置信息，这些配置信息会在虚拟机发生故障切换时被使用。

## 示例

### 示例 1
```
PS C:\> Get-VMNetworkAdapterFailoverConfiguration VM01
```

这个示例获取了所有连接到名为VM01的虚拟机的虚拟网络适配器的故障转移IP地址配置信息。

### 示例 2
```
PS C:\> Get-VMNetworkAdapterFailoverConfiguration VM01 -VMNetworkAdapterName NetworkAdapter
```

这个示例获取了名为VM01的虚拟机上、名为NetworkAdapter的虚拟网络适配器的故障转移IP地址配置信息。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个 Hyper-V 主机，以便从中获取虚拟网络适配器的 IP 地址配置信息。允许使用 NetBIOS 名称、IP 地址和完全限定域名作为主机标识。默认值为本地计算机；可以使用 `localhost` 或点号（.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定您希望获取其虚拟网络适配器IP地址配置的虚拟机。

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
指定您想要获取其虚拟网络适配器IP地址配置的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMNetworkAdapter
指定您想要获取其IP地址配置的虚拟网络适配器。

```yaml
Type: VMNetworkAdapter[]
Parameter Sets: ResourceObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMNetworkAdapterName
指定要获取其IP地址配置的虚拟网络适配器的名称。

```yaml
Type: String
Parameter Sets: VMName, VMObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV POWERShell.VMNetworkAdapterFailoverSetting

## 备注

## 相关链接

