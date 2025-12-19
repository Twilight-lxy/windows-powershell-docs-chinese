---
external help file: Microsoft.Windows.Bcd.Cmdlets.dll-Help.xml
Module Name: Microsoft.Windows.Bcd.Cmdlets
ms.date: 02/21/2024
online version: https://learn.microsoft.com/powershell/module/microsoft.windows.bcd.cmdlets/set-bcddebugsettings?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-BcdDebugSettings
---

# 设置 BCD 调试选项

## 摘要
{{ 填写剧情简介 }}

## 语法

### SerialWithDebugPort
```
Set-BcdDebugSettings [[-Store] <BcdStoreInfo>] [-Baudrate <Int64>] -DebugPort <Int64> [-Serial]
 [-StartPolicy <StartPolicy>] [-NoUserModeExceptions] [-Force] [<CommonParameters>]
```

### SerialWithOutDebugPort
```
Set-BcdDebugSettings [[-Store] <BcdStoreInfo>] [-Serial] [-StartPolicy <StartPolicy>] [-NoUserModeExceptions]
 [-Force] [<CommonParameters>]
```

### NETWithKey
```
Set-BcdDebugSettings [[-Store] <BcdStoreInfo>] -Port <Int64> -HostIp <String> [-Net] -Key <String> [-NoDhcp]
 [-StartPolicy <StartPolicy>] [-NoUserModeExceptions] [-Force] [<CommonParameters>]
```

### NETCreateKey
```
Set-BcdDebugSettings [[-Store] <BcdStoreInfo>] -Port <Int64> -HostIp <String> [-Net] [-NewKey] [-NoDhcp]
 [-StartPolicy <StartPolicy>] [-NoUserModeExceptions] [-Force] [<CommonParameters>]
```

### 1394
```
Set-BcdDebugSettings [[-Store] <BcdStoreInfo>] -Channel <Int64> [-Ieee1394] [-StartPolicy <StartPolicy>]
 [-NoUserModeExceptions] [-Force] [<CommonParameters>]
```

### USB
```
Set-BcdDebugSettings [[-Store] <BcdStoreInfo>] [-Usb] [-TargetName <String>] [-StartPolicy <StartPolicy>]
 [-NoUserModeExceptions] [-Force] [<CommonParameters>]
```

### 本地
```
Set-BcdDebugSettings [[-Store] <BcdStoreInfo>] [-Local] [-StartPolicy <StartPolicy>] [-NoUserModeExceptions]
 [-Force] [<CommonParameters>]
```

## 描述
{{ 请填写描述内容 }}

## 示例

### 示例 1
```powershell
PS C:\> {{ Add example code here }}
```

{{ 在这里添加示例描述 }}

## 参数

### -Baudrate
{{ 填写波特率描述 }}

```yaml
Type: System.Int64
Parameter Sets: SerialWithDebugPort
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Channel
{{ 填写频道描述 }}

```yaml
Type: System.Int64
Parameter Sets: 1394
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DebugPort
{{ 填写调试端口的描述 }}

```yaml
Type: System.Int64
Parameter Sets: SerialWithDebugPort
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
{{ 填充力量描述 }}

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HostIp
{{ 填写主机IP地址的描述 }}

```yaml
Type: System.String
Parameter Sets: NETWithKey, NETCreateKey
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Ieee1394
{{ 填写 Ieee1394 的描述 }}

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: 1394
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Key
{{ 填写键描述 }}

```yaml
Type: System.String
Parameter Sets: NETWithKey
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Local
{{ 填写本地描述 }}

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: Local
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Net
请帮我填写网络描述（Fill in the network description）。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: NETWithKey, NETCreateKey
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NewKey
请帮我填写「NewKey 的描述」。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: NETCreateKey
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoDhcp
请帮我填写 {{ Fill NoDhcp Description }}

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: NETWithKey, NETCreateKey
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoUserModeExceptions
{{ Fill NoUserModeExceptions Description }}

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: NoUmex

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Port
请填写端口描述：

```yaml
Type: System.Int64
Parameter Sets: NETWithKey, NETCreateKey
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Serial
{{ 填写序列描述 }}

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: SerialWithDebugPort, SerialWithOutDebugPort
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StartPolicy
{{ 填写政策描述开始 }}

```yaml
Type: Microsoft.Windows.Bcd.Cmdlets.BcdExtensions.StartPolicy
Parameter Sets: (All)
Aliases:
Accepted values: Active, AutoEnable, Disable

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Store
{{ 填写店铺描述 }}

```yaml
Type: Microsoft.Windows.Bcd.Cmdlets.BcdExtensions.BcdStoreInfo
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -TargetName
{{ 填写目标名称及描述 }}

```yaml
Type: System.String
Parameter Sets: Usb
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Usb
{{ 填写U盘描述 }}

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: Usb
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.Windows.Bcd Cmdlets.BcdExtensions.BcdStoreInfo

## 输出

### System.Object
## 备注

## 相关链接
