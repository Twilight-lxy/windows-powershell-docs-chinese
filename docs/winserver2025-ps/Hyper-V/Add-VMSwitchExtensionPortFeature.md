---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/add-vmswitchextensionportfeature?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-VMSwitchExtensionPortFeature
---

# 添加-VMSwitchExtensionPortFeature

## 摘要
为虚拟网络适配器添加扩展功能。

## 语法

### VMName（默认值）
```
Add-VMSwitchExtensionPortFeature [-VMName] <String[]> [-VMNetworkAdapterName <String>]
 [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 -VMSwitchExtensionFeature <VMSwitchExtensionPortFeature[]> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ResourceObject
```
Add-VMSwitchExtensionPortFeature [-VMNetworkAdapter] <VMNetworkAdapterBase[]>
 -VMSwitchExtensionFeature <VMSwitchExtensionPortFeature[]> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ManagementOS
```
Add-VMSwitchExtensionPortFeature [-ManagementOS] [-VMNetworkAdapterName <String>] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 -VMSwitchExtensionFeature <VMSwitchExtensionPortFeature[]> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### ExternalPort
```
Add-VMSwitchExtensionPortFeature [-ExternalPort] [-SwitchName <String>] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 -VMSwitchExtensionFeature <VMSwitchExtensionPortFeature[]> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### VMObject
```
Add-VMSwitchExtensionPortFeature [-VMNetworkAdapterName <String>] [-VM] <VirtualMachine[]>
 -VMSwitchExtensionFeature <VMSwitchExtensionPortFeature[]> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Add-VMSwitchExtensionPortFeature` cmdlet 可将虚拟交换机扩展所支持的功能添加到虚拟机的网络适配器中。此外，该 cmdlet 还会配置内置的虚拟交换机功能。

## 示例

#### 示例 1
```
PS C:\> $feature = Get-VMSystemSwitchExtensionPortFeature -FeatureName "Ethernet Switch Port Security Settings"
PS C:\> $feature.SettingData.EnableDhcpGuard = $true
PS C:\> $feature.SettingData.EnableRouterGuard = $true
PS C:\> Add-VMSwitchExtensionPortFeature -VMName VM2 -VMSwitchExtensionFeature $feature
```

为虚拟机VM2添加了一项新功能。该功能是端口安全机制，由“Microsoft Virtual Ethernet Switch Native Extension”扩展程序提供支持。

## 参数

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: VMName, ManagementOS, ExternalPort
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个Hyper-V主机，在这些主机上需要为虚拟网络适配器添加某个功能。允许使用NetBIOS名称、IP地址或完全限定域名进行标识。默认值是本地计算机。可以使用“localhost”或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName, ManagementOS, ExternalPort
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

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
Parameter Sets: VMName, ManagementOS, ExternalPort
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ExternalPort
指定连接到外部网络适配器的虚拟交换机端口。

```yaml
Type: SwitchParameter
Parameter Sets: ExternalPort
Aliases:

Required: True
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ManagementOS
指定该功能需要添加到管理型（即父级或宿主）操作系统中。

```yaml
Type: SwitchParameter
Parameter Sets: ManagementOS
Aliases:

Required: True
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定要将一个对象传递给管道，该对象代表要添加的特征。

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

### -SwitchName
指定虚拟交换机的名称。

```yaml
Type: String
Parameter Sets: ExternalPort
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定要添加该功能的虚拟机。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定要添加该功能的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMNetworkAdapter
指定要为其添加该功能的虚拟机网络适配器。

```yaml
Type: VMNetworkAdapterBase[]
Parameter Sets: ResourceObject
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMNetworkAdapterName
指定要为其添加该功能的虚拟机网络适配器的名称。

```yaml
Type: String
Parameter Sets: VMName, ManagementOS, VMObject
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMSwitchExtensionFeature
指定要添加到虚拟交换机中的功能。您可以通过 `Get-VMSystemSwitchExtensionPortFeature` 命令获取此类功能对象，以便将新的配置添加到虚拟网络适配器中；或者使用 `Get-VMSwitchExtensionPortFeature` cmdlet 来更新现有的配置。

```yaml
Type: VMSwitchExtensionPortFeature[]
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell.VMSwitchExtensionPortFeature
如果指定了**-PassThru**选项的话……

## 备注

## 相关链接

