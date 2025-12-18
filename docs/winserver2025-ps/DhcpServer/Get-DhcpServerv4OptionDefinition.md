---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: PS_DhcpServerV4OptionDefinition_v1.0.0.cdxml-help.xml
Module Name: DhcpServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/dhcpserver/get-dhcpserverv4optiondefinition?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-DhcpServerv4OptionDefinition
---

# Get-DhcpServerv4OptionDefinition

## 摘要
获取指定选项ID对应的DHCPv4选项定义。

## 语法

```
Get-DhcpServerv4OptionDefinition [-ComputerName <String>] [[-OptionId] <UInt32[]>] [[-VendorClass] <String>]
 [-All] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-DhcpServerv4OptionDefinition` cmdlet 可以获取指定选项标识符（IDs）对应的 DHCPv4 选项定义信息。

如果您不指定 *OptionId* 参数，系统将返回所有非特定于某个供应商的选项定义。而 *VendorClass* 参数则作为过滤器，仅用于筛选属于指定供应商类别的选项定义。

如果您指定了“All”参数，那么将返回所有选项定义，包括针对特定供应商类别的选项定义。

如果您指定了 *All* 和 *OptionId* 参数，那么将返回所有的选项定义，包括那些具有指定选项 ID 的、特定于供应商类别的选项定义。

如果您指定了“All”和“VendorClass”这两个参数，那么“All”参数将被忽略。

## 示例

### 示例 1：获取标准的 DHCPv4 选项定义
```
PS C:\> Get-DhcpServerv4OptionDefinition -ComputerName "dhcpserver.contoso.com"
```

这个示例获取了在名为dhcpserver.contoso.com的计算机上运行的DHCP服务器服务中的标准（即非供应商特定的）DHCPv4选项定义。

### 示例 2：获取所有 DHCPv4 选项的定义
```
PS C:\> Get-DhcpServerv4OptionDefinition -ComputerName "dhcpserver.contoso.com" -All
```

这个示例获取了DHCP服务器服务上所有的DHCPv4选项定义，包括供应商特定的选项定义。

### 示例 3：获取某个 DHCPv4 选项的定义
```
PS C:\> Get-DhcpServerv4OptionDefinition -ComputerName "dhcpserver.contoso.com" -OptionId 23
```

这个示例获取了指定选项的 DHCPv4 选项定义。

### 示例 4：获取某个供应商类别的所有 DHCPv4 选项定义
```
PS C:\> Get-DhcpServerv4OptionDefinition -ComputerName "dhcpserver.contoso.com" -VendorClass "Microsoft Windows Options"
```

这个例子获取了指定供应商类别的所有DHCPv4选项定义。

## 参数

### -All
表示此cmdlet可以获取DHCP服务器服务上的所有选项定义，包括供应商特定的选项定义。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行那些需要较长时间才能完成的命令。该cmdlet会立即返回一个表示该作业的对象，然后显示命令提示符。在作业完成期间，您可以继续在当前会话中工作。要管理该作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。有关Windows PowerShell®后台作业的更多信息，请参阅[about_Jobs](https://go.microsoft.com/fwlink/?LinkID=113251)。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。您可以输入计算机名称或会话对象（例如，通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的输出结果）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定运行动态主机配置协议（DHCP）服务器服务的目标计算机的DNS名称、IPv4地址或IPv6地址。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Cn

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OptionId
指定需要获取其选项定义的那些选项的数字标识符。如果您不指定此参数，将返回所有 DHCPv4 选项的定义。

```yaml
Type: UInt32[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略此参数或输入值 `0`，Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VendorClass
仅返回指定供应商类别的选项定义。

```yaml
Type: String
Parameter Sets: (All)
Aliases: Name

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4OptionValue
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名称。

## 输出

### Microsoft.ManagementInfrastructure.CimInstance#root/Microsoft/Windows/DHCP/DhcpServerv4OptionDefinition[]
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径表示底层 WMI 对象的命名空间和类名称。

## 备注

## 相关链接

[Add-DhcpServerv4OptionDefinition](./Add-DhcpServerv4OptionDefinition.md)

[Remove-DhcpServerv4OptionDefinition](./Remove-DhcpServerv4OptionDefinition.md)

[Set-DhcpServerv4OptionDefinition](./Set-DhcpServerv4OptionDefinition.md)

