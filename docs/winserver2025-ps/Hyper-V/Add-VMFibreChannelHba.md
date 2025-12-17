---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/add-vmfibrechannelhba?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-VMFibreChannelHba
---

# Add-VMFibreChannelHba

## 摘要
向虚拟机添加一个虚拟光纤通道（Fibre Channel）主机总线适配器。

## 语法

### VMName 和 GenerateWwn（默认值）
```
Add-VMFibreChannelHba [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String> [-SanName] <String> [-GenerateWwn] [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### VMName 与手动分配的 WWN（World Wide Name）
```
Add-VMFibreChannelHba [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String> [-SanName] <String> -WorldWideNodeNameSetA <String> -WorldWidePortNameSetA <String>
 -WorldWideNodeNameSetB <String> -WorldWidePortNameSetB <String> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### 虚拟机对象（VM Object）与GenerateWwn
```
Add-VMFibreChannelHba [-VM] <VirtualMachine[]> [-SanName] <String> [-GenerateWwn] [-Passthru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### 虚拟机对象（VM Object）和手动分配的世界范围唯一编号（WWN）
```
Add-VMFibreChannelHba [-VM] <VirtualMachine[]> [-SanName] <String> -WorldWideNodeNameSetA <String>
 -WorldWidePortNameSetA <String> -WorldWideNodeNameSetB <String> -WorldWidePortNameSetB <String> [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-VMFibreChannelHba` cmdlet 可以将一个虚拟光纤通道主机总线适配器添加到虚拟机中。

## 示例

#### 示例 1
```
PS C:\> Add-VMFibreChannelHba -VMName MyVM -SanName Production
```

这个示例将与虚拟存储区域网络“Production”关联的虚拟光纤通道主机总线适配器添加到名为“MyVM”的虚拟机中。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: VMName and GenerateWwn, VMName and manual WWN
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个Hyper-V主机，在这些主机上需要添加虚拟Fibre Channel主机总线适配器。可以使用NetBIOS名称、IP地址或完全限定域名来进行指定。默认值是本地计算机；可以通过使用“localhost”或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName and GenerateWwn, VMName and manual WWN
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您确认是否要执行该操作。

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
指定一个或多个具有执行此操作权限的用户账户。默认值是当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: VMName and GenerateWwn, VMName and manual WWN
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GenerateWwn
指定应自动生成光纤通道主机总线适配器的全球唯一名称（WWN）。一旦指定了这一点，就无法使用 **WorldWideNodeNameSetA**、**WorldWideNodeNameSetB**、**WorldWidePortNameSetA** 和 **WorldWidePortNameSetB** 这些参数了。

```yaml
Type: SwitchParameter
Parameter Sets: VMName and GenerateWwn, VM object and GenerateWwn
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定一个对象，该对象代表虚拟机；即将添加到该虚拟机上的虚拟光纤通道主机总线适配器需要通过该对象传递到后续处理流程中。

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

### -SanName
指定要与此虚拟光纤通道主机总线适配器关联的虚拟存储区域网络（SAN）名称。可以使用 **Get-VMSan** cmdlet 来获取主机上所有虚拟 SAN 的列表。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定要添加虚拟光纤通道主机总线适配器的虚拟机。

```yaml
Type: VirtualMachine[]
Parameter Sets: VM object and GenerateWwn, VM Object and manual WWN
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定要添加虚拟光纤通道主机总线适配器的虚拟机的名称。

```yaml
Type: String
Parameter Sets: VMName and GenerateWwn, VMName and manual WWN
Aliases:

Required: True
Position: 0
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

### -WorldWideNodeNameSetA
指定要与要添加的 Fibre Channel 主机总线适配器关联的地址 A 的全球唯一节点名称。

```yaml
Type: String
Parameter Sets: VMName and manual WWN, VM Object and manual WWN
Aliases: Wwnn1

Required: True
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WorldWideNodeNameSetB
指定要与要添加的 Fibre Channel 主机总线适配器关联的地址 B 的全球唯一节点名称。

```yaml
Type: String
Parameter Sets: VMName and manual WWN, VM Object and manual WWN
Aliases: Wwnn2

Required: True
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WorldWidePortNameSetA
指定要与要添加的 Fibre Channel 主机总线适配器关联的地址 A 的全球范围内的端口名称。

```yaml
Type: String
Parameter Sets: VMName and manual WWN, VM Object and manual WWN
Aliases: Wwpn1

Required: True
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WorldWidePortNameSetB
指定要与要添加的Fibre Channel主机总线适配器关联的地址B的全球端口号名称。

```yaml
Type: String
Parameter Sets: VMName and manual WWN, VM Object and manual WWN
Aliases: Wwpn2

Required: True
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无

## 输出

### 无
默认值

### Microsoft.HyperV.PowerShell.VirtualMachine
如果指定了**-PassThru**选项。

## 备注

## 相关链接

